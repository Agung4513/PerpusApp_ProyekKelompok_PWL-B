from fastapi import APIRouter, Depends, HTTPException, Query, status, File, UploadFile
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, desc, asc
from datetime import datetime
from typing import List
import shutil
import os
import models
from dependencies import get_db, cek_admin

router = APIRouter(prefix="", tags=["Katalog & Manajemen Buku"])

# Pastikan folder uploads ada
os.makedirs("uploads", exist_ok=True)

# ==========================================
# 1. KATEGORI & PENULIS (Master Data)
# ==========================================
@router.get("/kategori")
def ambil_semua_kategori(db: Session = Depends(get_db)):
    return db.query(models.Kategori).all()

@router.get("/penulis")
def ambil_semua_penulis(db: Session = Depends(get_db)):
    return db.query(models.Penulis).all()

@router.post("/penulis")
def tambah_penulis(nama_penulis: str = Query(...), db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    penulis_baru = models.Penulis(nama_penulis=nama_penulis)
    db.add(penulis_baru)
    db.commit()
    return {"pesan": f"Penulis '{nama_penulis}' berhasil ditambahkan!"}

# ==========================================
# 2. FILTER & PENCARIAN BUKU
# ==========================================
@router.get("/buku")
def cari_dan_filter_buku(
    keyword: str = Query(None, description="Cari judul atau ISBN"),
    kategori: str = Query(None, description="Filter berdasarkan nama kategori"),
    tahun: int = Query(None, description="Filter berdasarkan tahun terbit"),
    sort: str = Query("terbaru", description="Opsi: judul_asc, judul_desc, terbaru, terlama"),
    page: int = Query(1, ge=1, description="Halaman ke-berapa"),
    limit: int = Query(10, ge=1, le=50, description="Jumlah data per halaman"),
    db: Session = Depends(get_db)
):
    query = db.query(models.Buku).options(
        joinedload(models.Buku.kategori),
        joinedload(models.Buku.penulis) 
    )

    if keyword:
        search_term = f"%{keyword}%"
        query = query.filter(
            or_(
                models.Buku.judul.ilike(search_term),
                models.Buku.isbn.ilike(search_term)
            )
        )

    if kategori:
        query = query.join(models.Kategori).filter(models.Kategori.nama_kategori.ilike(f"%{kategori}%"))

    if tahun:
        query = query.filter(models.Buku.tahun_terbit == tahun)

    if sort == "judul_asc":
        query = query.order_by(asc(models.Buku.judul))
    elif sort == "judul_desc":
        query = query.order_by(desc(models.Buku.judul))
    elif sort == "terbaru":
        query = query.order_by(desc(models.Buku.tahun_terbit))
    elif sort == "terlama":
        query = query.order_by(asc(models.Buku.tahun_terbit))

    total_data = query.count()
    offset = (page - 1) * limit
    buku_list = query.offset(offset).limit(limit).all()

    return {
        "metadata": {
            "total_data": total_data,
            "page": page,
            "limit": limit,
            "total_page": (total_data + limit - 1) // limit
        },
        "data": buku_list
    }

# ==========================================
# 3. CRUD BUKU DASAR (Dengan Penulis)
# ==========================================
@router.post("/buku")
def tambah_buku(
    isbn: str = Query(...), 
    judul: str = Query(...), 
    tahun_terbit: int = Query(...), 
    id_kategori: int = Query(...), 
    stok_awal: int = Query(0, description="Jumlah stok fisik buku saat ini"),
    id_penulis_list: List[int] = Query([], description="Daftar ID Penulis buku ini"), 
    db: Session = Depends(get_db), 
    admin: models.Akun = Depends(cek_admin)
):
    tahun_sekarang = datetime.now().year
    if tahun_terbit > tahun_sekarang or tahun_terbit < 1000:
        raise HTTPException(status_code=400, detail=f"Tahun terbit harus antara 1000 - {tahun_sekarang}.")
    
    buku_ada = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if buku_ada:
        raise HTTPException(status_code=400, detail=f"Buku dengan ISBN {isbn} sudah ada!")

    penulis_terkait = db.query(models.Penulis).filter(models.Penulis.id_penulis.in_(id_penulis_list)).all()

    buku_baru = models.Buku(
        isbn=isbn, 
        judul=judul, 
        tahun_terbit=tahun_terbit, 
        id_kategori=id_kategori,
        stok_total=stok_awal,
        stok_tersedia=stok_awal,
        penulis=penulis_terkait 
    )
    db.add(buku_baru)
    db.commit()
    return {"pesan": f"Buku '{judul}' berhasil ditambahkan dengan {len(penulis_terkait)} penulis!"}

@router.put("/buku/{isbn}")
def edit_buku(
    isbn: str, 
    judul_baru: str, 
    tahun_baru: int, 
    id_penulis_list: List[int] = Query([], description="Daftar ID Penulis buku ini"),
    db: Session = Depends(get_db), 
    admin: models.Akun = Depends(cek_admin)
):
    buku = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan!")
    
    buku.judul = judul_baru
    buku.tahun_terbit = tahun_baru
    
    if id_penulis_list:
        penulis_terkait = db.query(models.Penulis).filter(models.Penulis.id_penulis.in_(id_penulis_list)).all()
        buku.penulis = penulis_terkait 

    db.commit()
    return {"pesan": f"Buku ISBN {isbn} berhasil diperbarui!"}

@router.delete("/buku/{isbn}")
def hapus_buku(isbn: str, db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    buku = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan!")
    
    peminjaman_aktif = db.query(models.Peminjaman).filter(
        models.Peminjaman.isbn == isbn,
        models.Peminjaman.status_peminjaman.in_(['Menunggu', 'Dipinjam', 'Menunggu Konfirmasi Kembali'])
    ).first()
    
    if peminjaman_aktif:
        raise HTTPException(status_code=400, detail="Buku sedang dalam transaksi aktif!")

    db.delete(buku) 
    db.commit()
    return {"pesan": f"Buku '{buku.judul}' berhasil dihapus."}

# ==========================================
# 4. UPDATE STOK & UPLOAD GAMBAR
# ==========================================
@router.put("/buku/{isbn}/stok")
def update_stok_buku(
    isbn: str,
    stok_tambahan: int = Query(..., description="Gunakan angka minus (misal: -2) untuk mengurangi stok"),
    db: Session = Depends(get_db),
    admin: models.Akun = Depends(cek_admin)
):
    buku = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan!")

    buku.stok_total += stok_tambahan
    buku.stok_tersedia += stok_tambahan

    if buku.stok_total < 0 or buku.stok_tersedia < 0:
        raise HTTPException(status_code=400, detail="Operasi gagal! Stok akhir tidak boleh kurang dari 0.")

    log = models.LogAktivitas(
        username=admin.username,
        aksi="Update Stok",
        detail=f"Mengubah stok ISBN '{isbn}' sejumlah {stok_tambahan}."
    )
    db.add(log)
    db.commit()
    db.refresh(buku)

    return {
        "pesan": "Stok berhasil diperbarui!",
        "isbn": buku.isbn,
        "stok_total_sekarang": buku.stok_total,
        "stok_tersedia_sekarang": buku.stok_tersedia
    }

@router.post("/buku/{isbn}/upload-sampul")
def upload_sampul_buku(
    isbn: str, 
    file: UploadFile = File(...), 
    db: Session = Depends(get_db), 
    admin: models.Akun = Depends(cek_admin)
):
    buku = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan!")

    # Validasi tipe file (hanya gambar)
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File harus berupa gambar (JPEG/PNG).")

    # Bikin nama file unik agar tidak bentrok
    ekstensi = file.filename.split(".")[-1]
    nama_file_baru = f"cover_{isbn}.{ekstensi}"
    lokasi_simpan = f"uploads/{nama_file_baru}"

    # Simpan file ke folder
    with open(lokasi_simpan, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Simpan URL/path ke database
    # Saat dipanggil di frontend, url-nya menjadi: http://127.0.0.1:8000/uploads/...
    buku.gambar_sampul = f"/uploads/{nama_file_baru}"
    
    db.commit()
    return {"pesan": "Gambar sampul berhasil diunggah!", "url_gambar": buku.gambar_sampul}
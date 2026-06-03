from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, desc, asc
from datetime import datetime
import models
from dependencies import get_db, cek_admin

router = APIRouter(prefix="", tags=["Katalog & Manajemen Buku"])

# ==========================================
# 1. KATEGORI (Fase 1)
# ==========================================
@router.get("/kategori")
def ambil_semua_kategori(db: Session = Depends(get_db)):
    return db.query(models.Kategori).all()

# ==========================================
# 2. FILTER & PENCARIAN BUKU (Endpoint 18 - 🔴 Tinggi)
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
    # Gabungkan (join) dengan tabel Kategori agar bisa filter nama kategori
    query = db.query(models.Buku).options(joinedload(models.Buku.kategori))

    # 1. Pencarian (Keyword)
    if keyword:
        search_term = f"%{keyword}%"
        query = query.filter(
            or_(
                models.Buku.judul.ilike(search_term),
                models.Buku.isbn.ilike(search_term)
            )
        )

    # 2. Filter Kategori
    if kategori:
        query = query.join(models.Kategori).filter(models.Kategori.nama_kategori.ilike(f"%{kategori}%"))

    # 3. Filter Tahun Terbit
    if tahun:
        query = query.filter(models.Buku.tahun_terbit == tahun)

    # 4. Pengurutan (Sorting)
    if sort == "judul_asc":
        query = query.order_by(asc(models.Buku.judul))
    elif sort == "judul_desc":
        query = query.order_by(desc(models.Buku.judul))
    elif sort == "terbaru":
        query = query.order_by(desc(models.Buku.tahun_terbit))
    elif sort == "terlama":
        query = query.order_by(asc(models.Buku.tahun_terbit))

    # 5. Penomoran Halaman (Pagination)
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
# 3. CRUD BUKU DASAR (Fase 1)
# ==========================================
@router.post("/buku")
def tambah_buku(
    isbn: str, 
    judul: str, 
    tahun_terbit: int, 
    id_kategori: int, 
    stok_awal: int = Query(0, description="Jumlah stok fisik buku saat ini"),
    db: Session = Depends(get_db), 
    admin: models.Akun = Depends(cek_admin)
):
    tahun_sekarang = datetime.now().year
    if tahun_terbit > tahun_sekarang or tahun_terbit < 1000:
        raise HTTPException(status_code=400, detail=f"Tahun terbit harus antara 1000 - {tahun_sekarang}.")
    
    buku_ada = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if buku_ada:
        raise HTTPException(status_code=400, detail=f"Buku dengan ISBN {isbn} sudah ada!")

    buku_baru = models.Buku(
        isbn=isbn, 
        judul=judul, 
        tahun_terbit=tahun_terbit, 
        id_kategori=id_kategori,
        stok_total=stok_awal,
        stok_tersedia=stok_awal
    )
    db.add(buku_baru)
    db.commit()
    return {"pesan": f"Buku '{judul}' berhasil ditambahkan dengan {stok_awal} stok!"}

@router.put("/buku/{isbn}")
def edit_buku(isbn: str, judul_baru: str, tahun_baru: int, db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    buku = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan!")
    
    buku.judul = judul_baru
    buku.tahun_terbit = tahun_baru
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
# 4. UPDATE STOK BUKU (Endpoint 19 - 🔴 Tinggi)
# ==========================================
@router.put("/buku/{isbn}/stok")
def update_stok_buku(
    isbn: str,
    stok_tambahan: int = Query(..., description="Gunakan angka minus (misal: -2) untuk mengurangi stok, dan positif untuk menambah"),
    db: Session = Depends(get_db),
    admin: models.Akun = Depends(cek_admin)
):
    buku = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan!")

    # Kalkulasi stok
    buku.stok_total += stok_tambahan
    buku.stok_tersedia += stok_tambahan

    # Validasi stok tidak boleh minus
    if buku.stok_total < 0 or buku.stok_tersedia < 0:
        raise HTTPException(status_code=400, detail="Operasi gagal! Stok akhir tidak boleh kurang dari 0.")

    # Catat aksi ini ke dalam tabel LogAktivitas
    log = models.LogAktivitas(
        username=admin.username,
        aksi="Update Stok",
        detail=f"Mengubah stok ISBN '{isbn}' sejumlah {stok_tambahan}. Stok total kini: {buku.stok_total}"
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
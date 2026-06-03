from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from datetime import datetime
import models
from dependencies import get_db, cek_user_aktif

router = APIRouter(prefix="/pinjam", tags=["Transaksi (Anggota)"])

@router.post("/{isbn}")
def ajukan_pinjaman(isbn: str, db: Session = Depends(get_db), current_user: models.Akun = Depends(cek_user_aktif)):
    if current_user.role != "anggota":
        raise HTTPException(status_code=403, detail="Hanya anggota yang bisa meminjam!")

    denda_aktif = db.query(models.Peminjaman).filter(
        models.Peminjaman.id_anggota == current_user.profil.id_anggota,
        models.Peminjaman.status_denda == "Belum Lunas"
    ).first()
    if denda_aktif:
        raise HTTPException(status_code=400, detail="Anda memiliki denda belum lunas!")

    buku = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan!")

    id_anggota = current_user.profil.id_anggota

    pinjaman_aktif = db.query(models.Peminjaman).filter(
        models.Peminjaman.id_anggota == id_anggota,
        models.Peminjaman.isbn == isbn,
        models.Peminjaman.status_peminjaman.in_(['Menunggu', 'Dipinjam', 'Menunggu Konfirmasi Kembali'])
    ).first()
    if pinjaman_aktif:
        raise HTTPException(status_code=400, detail="Anda sedang meminjam/mengantre buku ini!")

    total = db.query(models.Peminjaman).filter(
        models.Peminjaman.id_anggota == id_anggota,
        models.Peminjaman.status_peminjaman.in_(['Menunggu', 'Dipinjam', 'Menunggu Konfirmasi Kembali'])
    ).count()
    if total >= 3:
        raise HTTPException(status_code=400, detail="Batas maksimal 3 buku!")

    transaksi = models.Peminjaman(
        id_anggota=id_anggota,
        isbn=isbn,
        status_peminjaman="Menunggu",
        tanggal_pinjam=datetime.now()
    )
    db.add(transaksi)
    db.commit()
    return {"pesan": "Permintaan pinjam diajukan. Menunggu persetujuan Admin!"}

@router.get("/riwayat")
def riwayat_pinjaman_saya(db: Session = Depends(get_db), current_user: models.Akun = Depends(cek_user_aktif)):
    if current_user.role != "anggota":
        raise HTTPException(status_code=403, detail="Khusus anggota.")
    
    return db.query(models.Peminjaman).options(
        joinedload(models.Peminjaman.buku)
    ).filter(
        models.Peminjaman.id_anggota == current_user.profil.id_anggota
    ).order_by(models.Peminjaman.id_peminjaman.desc()).all()

@router.put("/{id_peminjaman}/ajukan-kembali")
def ajukan_pengembalian(id_peminjaman: int, db: Session = Depends(get_db), current_user: models.Akun = Depends(cek_user_aktif)):
    if current_user.role != "anggota":
        raise HTTPException(status_code=403, detail="Hanya anggota!")

    transaksi = db.query(models.Peminjaman).options(
        joinedload(models.Peminjaman.buku)
    ).filter(
        models.Peminjaman.id_peminjaman == id_peminjaman,
        models.Peminjaman.id_anggota == current_user.profil.id_anggota,
        models.Peminjaman.status_peminjaman == "Dipinjam"
    ).first()
    
    if not transaksi:
        raise HTTPException(status_code=404, detail="Transaksi tidak valid!")
    
    transaksi.status_peminjaman = "Menunggu Konfirmasi Kembali"
    db.commit()
    return {"pesan": f"Pengembalian '{transaksi.buku.judul}' diajukan. Tunggu konfirmasi Admin."}
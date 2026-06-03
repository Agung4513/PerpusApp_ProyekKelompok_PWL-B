from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
import models
from dependencies import get_db, cek_admin, cek_user_aktif

router = APIRouter(prefix="", tags=["Denda"])

@router.get("/admin/denda")
def lihat_semua_denda(db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    return db.query(models.Peminjaman).options(
        joinedload(models.Peminjaman.peminjam),
        joinedload(models.Peminjaman.buku)
    ).filter(models.Peminjaman.total_denda > 0).order_by(models.Peminjaman.status_denda).all()

@router.get("/denda/saya")
def lihat_denda_saya(db: Session = Depends(get_db), current_user: models.Akun = Depends(cek_user_aktif)):
    if current_user.role != "anggota":
        raise HTTPException(status_code=403, detail="Khusus anggota.")
    
    denda_list = db.query(models.Peminjaman).options(
        joinedload(models.Peminjaman.buku)
    ).filter(
        models.Peminjaman.id_anggota == current_user.profil.id_anggota,
        models.Peminjaman.total_denda > 0
    ).all()
    
    total = sum(d.total_denda for d in denda_list if d.status_denda == "Belum Lunas")
    return {
        "daftar_denda": denda_list,
        "total_belum_lunas": total,
        "pesan": "Lunasi denda sebelum meminjam buku baru." if total > 0 else "Semua denda lunas!"
    }

@router.put("/admin/denda/{id_peminjaman}/bayar")
def konfirmasi_bayar_denda(id_peminjaman: int, db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    transaksi = db.query(models.Peminjaman).filter(models.Peminjaman.id_peminjaman == id_peminjaman).first()
    if not transaksi:
        raise HTTPException(status_code=404, detail="Transaksi tidak ditemukan!")
    if transaksi.status_denda != "Belum Lunas":
        raise HTTPException(status_code=400, detail="Tidak ada denda yang perlu dibayar!")
    
    transaksi.status_denda = "Lunas"
    db.commit()
    return {"pesan": f"Denda Rp {transaksi.total_denda:,} telah dikonfirmasi lunas."}
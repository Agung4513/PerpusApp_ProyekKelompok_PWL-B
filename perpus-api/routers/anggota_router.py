from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models, auth
from dependencies import get_db, cek_user_aktif
from sqlalchemy import func

router = APIRouter(prefix="/anggota", tags=["Profil & Akun Anggota"])

# Skema data (JSON Body) untuk edit profil
class ProfilUpdate(BaseModel):
    nama_baru: str
    no_telepon_baru: str

# Skema data (JSON Body) untuk ganti password
class PasswordUpdate(BaseModel):
    password_lama: str
    password_baru: str

@router.get("/profil")
def lihat_profil_saya(current_user: models.Akun = Depends(cek_user_aktif), db: Session = Depends(get_db)):
    if current_user.role != "anggota":
        raise HTTPException(status_code=403, detail="Hanya anggota yang memiliki profil.")
    
    # Mengambil data dari tabel Anggota yang berelasi dengan akun yang sedang login
    profil = current_user.profil
    
    # Hitung total denda yang belum lunas khusus untuk anggota ini
    total_denda = db.query(func.sum(models.Peminjaman.total_denda)).filter(
        models.Peminjaman.id_anggota == profil.id_anggota,
        models.Peminjaman.status_denda == "Belum Lunas"
    ).scalar()

    return {
        "username": current_user.username,
        "nama_anggota": profil.nama_anggota,
        "no_telepon": profil.no_telepon,
        "role": current_user.role,
        "denda_belum_lunas": total_denda if total_denda else 0
    }

@router.put("/profil")
def edit_profil_saya(data: ProfilUpdate, current_user: models.Akun = Depends(cek_user_aktif), db: Session = Depends(get_db)):
    if current_user.role != "anggota":
        raise HTTPException(status_code=403, detail="Hanya anggota yang bisa mengedit profil.")
    
    profil = current_user.profil
    profil.nama_anggota = data.nama_baru
    profil.no_telepon = data.no_telepon_baru
    
    db.commit()
    db.refresh(profil)
    return {"pesan": "Profil berhasil diperbarui!", "nama_anggota": profil.nama_anggota}

@router.put("/ganti-password")
def ganti_password_saya(data: PasswordUpdate, current_user: models.Akun = Depends(cek_user_aktif), db: Session = Depends(get_db)):
    # 1. Cek apakah password lama yang dimasukkan benar
    if not auth.verify_password(data.password_lama, current_user.password_hash):
        raise HTTPException(status_code=400, detail="Password lama salah!")
    
    # 2. Hash password baru dan simpan ke database
    current_user.password_hash = auth.get_password_hash(data.password_baru)
    db.commit()
    
    return {"pesan": "Password berhasil diubah! Silakan login kembali dengan password baru."}
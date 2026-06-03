from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import models, auth
from dependencies import get_db

router = APIRouter(prefix="", tags=["Autentikasi"])

@router.post("/register")
def mendaftar_akun(username: str, password: str, nama_lengkap: str, no_telepon: str, db: Session = Depends(get_db)):
    user_ada = db.query(models.Akun).filter(models.Akun.username == username).first()
    if user_ada:
        raise HTTPException(status_code=400, detail="Username sudah terdaftar!")
    
    password_acak = auth.get_password_hash(password)
    user_baru = models.Akun(username=username, password_hash=password_acak, role="anggota")
    db.add(user_baru)
    db.commit()
    
    profil_baru = models.Anggota(nama_anggota=nama_lengkap, no_telepon=no_telepon, username=username)
    db.add(profil_baru)
    db.commit()
    
    return {"pesan": f"Akun '{username}' berhasil dibuat. Silakan login."}

@router.post("/login")
def masuk_akun(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Akun).filter(models.Akun.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Username atau password salah!")
    
    data_token = {"sub": user.username, "role": user.role}
    tiket = auth.create_access_token(data=data_token)
    return {"access_token": tiket, "token_type": "bearer", "role": user.role}
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import jwt
import models, auth
from database import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def cek_user_aktif(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token tidak valid")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token kadaluarsa atau tidak valid")
    
    user = db.query(models.Akun).filter(models.Akun.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User tidak ditemukan")
    return user

def cek_admin(current_user: models.Akun = Depends(cek_user_aktif)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Akses ditolak! Fitur ini khusus Admin.")
    return current_user
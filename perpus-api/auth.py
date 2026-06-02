from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

# Kunci Rahasia untuk mengenkripsi Token (Di dunia nyata, jangan sebarluaskan ini)
SECRET_KEY = "rahasia_super_perpustakaan_pwl" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 # Tiket valid selama 1 jam

# Alat pembuat hash password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """Mengecek apakah password ketikan user cocok dengan hash di database"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Mengubah password tulisan biasa menjadi hash acak"""
    return pwd_context.hash(password)

def create_access_token(data: dict):
    """Membuat tiket (token) untuk user yang berhasil login"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
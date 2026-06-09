from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from database import engine
import models

# 1. Import semua router dari folder routers
from routers.auth_router import router as auth_router
from routers.buku_router import router as buku_router
from routers.peminjaman_router import router as peminjaman_router
from routers.admin_router import router as admin_router
from routers.denda_router import router as denda_router
from routers.anggota_router import router as anggota_router 

# 2. Sinkronisasi Database
models.Base.metadata.create_all(bind=engine)

# Pastikan folder uploads tercipta saat server menyala
os.makedirs("uploads", exist_ok=True)

app = FastAPI(
    title="API RuangBaca V2", 
    description="Sistem Manajemen Perpustakaan Terpadu",
    version="2.0.0"
)

# 3. Pengaturan Keamanan CORS (Agar React bisa terkoneksi)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# [BARU] Mengekspos folder uploads agar gambar bisa diakses dari browser
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# 4. Daftarkan (Include) Semua Router
app.include_router(auth_router)
app.include_router(buku_router)
app.include_router(peminjaman_router)
app.include_router(admin_router)
app.include_router(denda_router)
app.include_router(anggota_router)

# 5. Endpoint Cek Status Server
@app.get("/", tags=["Sistem"])
def root():
    return {"pesan": "Backend RuangBaca siap melayani!", "status": "Online"}
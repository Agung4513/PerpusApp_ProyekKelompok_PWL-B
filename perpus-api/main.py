from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, joinedload
from datetime import datetime, timedelta
import jwt
import models, auth
from database import SessionLocal, engine

# Magic: Membuat semua tabel di database jika belum ada
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API RuangBaca V2", 
    description="Sistem Manajemen Perpustakaan Terpadu",
    version="2.0.0"
)

# Membuka gerbang untuk Frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# Gembok pintu utama untuk Endpoint yang dilindungi
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Dependensi Database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- FUNGSI SATPAM (AUTHORIZATION) ---
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


@app.get("/", tags=["Sistem"])
def root():
    return {"pesan": "Backend RuangBaca siap melayani!", "status": "Online"}


# ==========================================
# 1. FITUR AUTENTIKASI & AKUN
# ==========================================

@app.post("/register", tags=["Autentikasi"])
def mendaftar_akun(username: str, password: str, nama_lengkap: str, no_telepon: str, db: Session = Depends(get_db)):
    """Mendaftar akun baru. (Otomatis menjadi role 'anggota', menambal celah keamanan)"""
    user_ada = db.query(models.Akun).filter(models.Akun.username == username).first()
    if user_ada:
        raise HTTPException(status_code=400, detail="Username sudah terdaftar! Pilih yang lain.")
    
    password_acak = auth.get_password_hash(password)
    
    # 1. Buat Akun Utama
    user_baru = models.Akun(username=username, password_hash=password_acak, role="anggota")
    db.add(user_baru)
    db.commit() # Commit akun agar username bisa dipakai oleh profil anggota
    
    # 2. Buat Profil Anggota dan relasikan dengan akun di atas
    profil_baru = models.Anggota(nama_anggota=nama_lengkap, no_telepon=no_telepon, username=username)
    db.add(profil_baru)
    db.commit()
    
    return {"pesan": f"Hore! Akun '{username}' berhasil dibuat. Silakan login."}

@app.post("/login", tags=["Autentikasi"])
def masuk_akun(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Akun).filter(models.Akun.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Username atau password salah!")
    
    data_token = {"sub": user.username, "role": user.role}
    tiket = auth.create_access_token(data=data_token)
    return {"access_token": tiket, "token_type": "bearer", "role": user.role}


# ==========================================
# 2. FITUR KATALOG BUKU (CRUD)
# ==========================================

@app.get("/buku", tags=["Katalog Publik"])
def ambil_semua_buku(db: Session = Depends(get_db)):
    """Melihat daftar buku (Bisa diakses siapa saja tanpa login)"""
    return db.query(models.Buku).all()

@app.get("/kategori", tags=["Katalog Publik"])
def ambil_semua_kategori(db: Session = Depends(get_db)):
    """Melihat daftar kategori buku (untuk dropdown form)"""
    return db.query(models.Kategori).all()

@app.post("/buku", tags=["Manajemen Buku (Admin)"])
def tambah_buku(isbn: str, judul: str, tahun_terbit: int, id_kategori: int, db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    tahun_sekarang = datetime.now().year
    if tahun_terbit > tahun_sekarang or tahun_terbit < 1000:
        raise HTTPException(status_code=400, detail=f"Tahun terbit tidak valid! Harus antara 1000 - {tahun_sekarang}.")
        
    buku_ada = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if buku_ada:
        raise HTTPException(status_code=400, detail=f"Buku dengan ISBN {isbn} sudah ada!")

    buku_baru = models.Buku(isbn=isbn, judul=judul, tahun_terbit=tahun_terbit, id_kategori=id_kategori)
    db.add(buku_baru)
    db.commit()
    return {"pesan": f"Buku '{judul}' berhasil ditambahkan ke katalog!"}

@app.put("/buku/{isbn}", tags=["Manajemen Buku (Admin)"])
def edit_buku(isbn: str, judul_baru: str, tahun_baru: int, db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    buku = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan!")
    
    buku.judul = judul_baru
    buku.tahun_terbit = tahun_baru
    db.commit()
    return {"pesan": f"Buku ISBN {isbn} berhasil diperbarui!"}

@app.delete("/buku/{isbn}", tags=["Manajemen Buku (Admin)"])
def hapus_buku(isbn: str, db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    buku = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan!")
        
    peminjaman_aktif = db.query(models.Peminjaman).filter(
        models.Peminjaman.isbn == isbn,
        models.Peminjaman.status_peminjaman.in_(['Menunggu', 'Dipinjam', 'Menunggu Konfirmasi Kembali'])
    ).first()
    
    if peminjaman_aktif:
        raise HTTPException(status_code=400, detail="TOLAK: Buku sedang dalam transaksi peminjaman aktif!")

    db.delete(buku)
    db.commit()
    return {"pesan": f"Buku '{buku.judul}' resmi dihapus."}


# ==========================================
# 3. FITUR PEMINJAMAN (ANGGOTA)
# ==========================================

@app.post("/pinjam/{isbn}", tags=["Transaksi (Anggota)"])
def ajukan_pinjaman(isbn: str, db: Session = Depends(get_db), current_user: models.Akun = Depends(cek_user_aktif)):
    if current_user.role != "anggota":
        raise HTTPException(status_code=403, detail="Hanya anggota yang bisa meminjam buku!")

    # Cek apakah anggota punya denda belum lunas
    denda_aktif = db.query(models.Peminjaman).filter(
        models.Peminjaman.id_anggota == current_user.profil.id_anggota,
        models.Peminjaman.status_denda == "Belum Lunas"
    ).first()
    
    if denda_aktif:
        raise HTTPException(status_code=400, detail="TOLAK: Anda memiliki denda yang belum dilunasi! Silakan lunasi denda terlebih dahulu.")

    # Memastikan buku ada
    buku = db.query(models.Buku).filter(models.Buku.isbn == isbn).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan!")

    id_anggota_login = current_user.profil.id_anggota # Mengambil ID Anggota dari relasi
    
    # 1. Mengecek antrean diri sendiri untuk buku yang sama
    pinjaman_aktif = db.query(models.Peminjaman).filter(
        models.Peminjaman.id_anggota == id_anggota_login,
        models.Peminjaman.isbn == isbn,
        models.Peminjaman.status_peminjaman.in_(['Menunggu', 'Dipinjam', 'Menunggu Konfirmasi Kembali'])
    ).first()
    
    if pinjaman_aktif:
        raise HTTPException(status_code=400, detail="Anda sedang meminjam atau mengantre buku ini!")

    # 2. ATURAN BISNIS: Cek batas maksimal peminjaman (Maks 3 buku)
    total_pinjaman = db.query(models.Peminjaman).filter(
        models.Peminjaman.id_anggota == id_anggota_login,
        models.Peminjaman.status_peminjaman.in_(['Menunggu', 'Dipinjam', 'Menunggu Konfirmasi Kembali'])
    ).count()

    if total_pinjaman >= 3:
        raise HTTPException(status_code=400, detail="TOLAK: Anda sudah mencapai batas maksimal 3 buku (sedang dipinjam/antre). Kembalikan buku lama terlebih dahulu!")

    transaksi_baru = models.Peminjaman(
        id_anggota=id_anggota_login,
        isbn=isbn,
        status_peminjaman="Menunggu",
        tanggal_pinjam=datetime.now()
    )
    db.add(transaksi_baru)
    db.commit()
    
    return {"pesan": f"Permintaan pinjam buku diajukan. Menunggu persetujuan Admin!"}

@app.get("/pinjam/riwayat", tags=["Transaksi (Anggota)"])
def riwayat_pinjaman_saya(db: Session = Depends(get_db), current_user: models.Akun = Depends(cek_user_aktif)):
    """Melihat riwayat buku yang pernah/sedang dipinjam oleh user yang sedang login"""
    if current_user.role != "anggota":
         raise HTTPException(status_code=403, detail="Ini khusus tampilan anggota.")
         
    id_anggota_login = current_user.profil.id_anggota
    riwayat = db.query(models.Peminjaman).options(
        joinedload(models.Peminjaman.buku)
    ).filter(
        models.Peminjaman.id_anggota == id_anggota_login
    ).order_by(models.Peminjaman.id_peminjaman.desc()).all()
    return riwayat

@app.put("/pinjam/{id_peminjaman}/ajukan-kembali", tags=["Transaksi (Anggota)"])
def ajukan_pengembalian(id_peminjaman: int, db: Session = Depends(get_db), current_user: models.Akun = Depends(cek_user_aktif)):
    """Anggota mengajukan pengembalian buku yang sedang dipinjam"""
    if current_user.role != "anggota":
        raise HTTPException(status_code=403, detail="Hanya anggota yang bisa mengajukan pengembalian!")
    
    id_anggota_login = current_user.profil.id_anggota
    
    # Cari transaksi yang valid
    transaksi = db.query(models.Peminjaman).options(
        joinedload(models.Peminjaman.buku)
    ).filter(
        models.Peminjaman.id_peminjaman == id_peminjaman,
        models.Peminjaman.id_anggota == id_anggota_login,
        models.Peminjaman.status_peminjaman == "Dipinjam"
    ).first()
    
    if not transaksi:
        raise HTTPException(status_code=404, detail="Transaksi tidak ditemukan, bukan milik Anda, atau sudah tidak dalam status Dipinjam!")
    
    transaksi.status_peminjaman = "Menunggu Konfirmasi Kembali"
    db.commit()
    
    return {"pesan": f"Pengembalian buku '{transaksi.buku.judul}' berhasil diajukan. Silakan serahkan buku ke perpustakaan dan tunggu konfirmasi Admin."}


# ==========================================
# 4. FITUR KELOLA TRANSAKSI & USER (ADMIN)
# ==========================================

@app.get("/admin/peminjaman", tags=["Manajemen Transaksi (Admin)"])
def lihat_semua_transaksi(
    status: str = None,
    db: Session = Depends(get_db), 
    admin: models.Akun = Depends(cek_admin)
):
    """Admin melihat semua transaksi, bisa filter by status"""
    query = db.query(models.Peminjaman).options(
        joinedload(models.Peminjaman.peminjam),
        joinedload(models.Peminjaman.buku)
    )
    
    if status:
        query = query.filter(models.Peminjaman.status_peminjaman == status)
    
    return query.order_by(models.Peminjaman.id_peminjaman.desc()).all()

@app.put("/admin/peminjaman/{id_peminjaman}/status", tags=["Manajemen Transaksi (Admin)"])
def update_status_pinjaman(
    id_peminjaman: int, 
    status_baru: str, 
    durasi_hari: int = 7,
    db: Session = Depends(get_db), 
    admin: models.Akun = Depends(cek_admin)
):
    status_valid = ["Menunggu", "Dipinjam", "Menunggu Konfirmasi Kembali", "Dikembalikan", "Ditolak"]
    if status_baru not in status_valid:
        raise HTTPException(status_code=400, detail=f"Status harus salah satu dari: {status_valid}")

    transaksi = db.query(models.Peminjaman).filter(models.Peminjaman.id_peminjaman == id_peminjaman).first()
    if not transaksi:
        raise HTTPException(status_code=404, detail="Data transaksi tidak ditemukan!")

    sekarang = datetime.now()
    
    # === LOGIKA DENDA ===
    
    # Saat admin menyetujui peminjaman
    if status_baru == "Dipinjam" and transaksi.status_peminjaman == "Menunggu":
        if durasi_hari < 1 or durasi_hari > 30:
            raise HTTPException(status_code=400, detail="Durasi peminjaman harus antara 1-30 hari!")
        
        transaksi.tanggal_disetujui = sekarang
        transaksi.tanggal_jatuh_tempo = sekarang + timedelta(days=durasi_hari)
        transaksi.status_denda = "Tidak Ada"
    
    # Saat admin mengkonfirmasi pengembalian
    elif status_baru == "Dikembalikan" and transaksi.status_peminjaman in ["Dipinjam", "Menunggu Konfirmasi Kembali"]:
        transaksi.tanggal_kembali = sekarang
        
        # Hitung denda jika terlambat
        if transaksi.tanggal_jatuh_tempo and sekarang > transaksi.tanggal_jatuh_tempo:
            selisih = sekarang - transaksi.tanggal_jatuh_tempo
            hari_terlambat = selisih.days
            
            if hari_terlambat > 0:
                transaksi.total_denda = hari_terlambat * transaksi.denda_per_hari
                transaksi.status_denda = "Belum Lunas"
            else:
                transaksi.status_denda = "Lunas"
        else:
            transaksi.status_denda = "Lunas"

    transaksi.status_peminjaman = status_baru
    db.commit()
    db.refresh(transaksi)
    
    # Pesan tambahan jika ada denda
    pesan_tambahan = ""
    if transaksi.total_denda > 0 and transaksi.status_denda == "Belum Lunas":
        pesan_tambahan = f" Denda: Rp {transaksi.total_denda:,} (terlambat {(transaksi.tanggal_kembali - transaksi.tanggal_jatuh_tempo).days} hari)."
    
    return {"pesan": f"Status transaksi ID {id_peminjaman} diubah menjadi '{status_baru}'.{pesan_tambahan}"}

@app.get("/admin/anggota", tags=["Manajemen Transaksi (Admin)"])
def daftar_anggota(db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    return db.query(models.Anggota).all()


# ==========================================
# 5. FITUR DENDA
# ==========================================

@app.get("/admin/denda", tags=["Manajemen Denda (Admin)"])
def lihat_semua_denda(db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    """Admin melihat semua denda yang ada"""
    denda_list = db.query(models.Peminjaman).options(
        joinedload(models.Peminjaman.peminjam),
        joinedload(models.Peminjaman.buku)
    ).filter(
        models.Peminjaman.total_denda > 0
    ).order_by(models.Peminjaman.status_denda).all()
    
    return denda_list

@app.get("/denda/saya", tags=["Transaksi (Anggota)"])
def lihat_denda_saya(db: Session = Depends(get_db), current_user: models.Akun = Depends(cek_user_aktif)):
    """Anggota melihat denda miliknya sendiri"""
    if current_user.role != "anggota":
        raise HTTPException(status_code=403, detail="Hanya anggota yang bisa melihat denda!")
    
    id_anggota_login = current_user.profil.id_anggota
    
    denda_saya = db.query(models.Peminjaman).options(
        joinedload(models.Peminjaman.buku)
    ).filter(
        models.Peminjaman.id_anggota == id_anggota_login,
        models.Peminjaman.total_denda > 0
    ).all()
    
    total_belum_lunas = sum(d.total_denda for d in denda_saya if d.status_denda == "Belum Lunas")
    
    return {
        "daftar_denda": denda_saya,
        "total_belum_lunas": total_belum_lunas,
        "pesan": "Anda tidak bisa meminjam buku baru sebelum semua denda dilunasi." if total_belum_lunas > 0 else "Semua denda sudah lunas!"
    }

@app.put("/admin/denda/{id_peminjaman}/bayar", tags=["Manajemen Denda (Admin)"])
def konfirmasi_bayar_denda(id_peminjaman: int, db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    """Admin mengkonfirmasi pembayaran denda"""
    transaksi = db.query(models.Peminjaman).filter(models.Peminjaman.id_peminjaman == id_peminjaman).first()
    
    if not transaksi:
        raise HTTPException(status_code=404, detail="Data transaksi tidak ditemukan!")
    
    if transaksi.status_denda != "Belum Lunas":
        raise HTTPException(status_code=400, detail="Transaksi ini tidak memiliki denda yang perlu dibayar!")
    
    transaksi.status_denda = "Lunas"
    db.commit()
    
    return {"pesan": f"Pembayaran denda sebesar Rp {transaksi.total_denda:,} untuk transaksi ID {id_peminjaman} telah dikonfirmasi lunas."}
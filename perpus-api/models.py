from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime, timedelta

class Akun(Base):
    __tablename__ = "akun"
    username = Column(String(50), primary_key=True, index=True)
    password_hash = Column(String(255))
    role = Column(String(20), default="anggota")
    
    profil = relationship("Anggota", back_populates="akun", uselist=False)

class Anggota(Base):
    __tablename__ = "anggota"
    id_anggota = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama_anggota = Column(String(100))
    no_telepon = Column(String(20))
    username = Column(String(50), ForeignKey("akun.username")) 
    
    akun = relationship("Akun", back_populates="profil")
    peminjaman = relationship("Peminjaman", back_populates="peminjam")

class Kategori(Base):
    __tablename__ = "kategori"
    id_kategori = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama_kategori = Column(String(50))
    
    buku = relationship("Buku", back_populates="kategori")

class Buku(Base):
    __tablename__ = "buku"
    isbn = Column(String(20), primary_key=True, index=True)
    judul = Column(String(255))
    tahun_terbit = Column(Integer)
    id_kategori = Column(Integer, ForeignKey("kategori.id_kategori"))
    
    # === TAMBAHAN FASE 3 & 6 (STOK & GAMBAR) ===
    stok_total = Column(Integer, default=0)
    stok_tersedia = Column(Integer, default=0)
    gambar_sampul = Column(String(255), nullable=True) # Akan menyimpan nama/path file gambar
    
    kategori = relationship("Kategori", back_populates="buku")
    peminjaman = relationship("Peminjaman", back_populates="buku")

class Peminjaman(Base):
    __tablename__ = "peminjaman"
    id_peminjaman = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_anggota = Column(Integer, ForeignKey("anggota.id_anggota"))
    isbn = Column(String(20), ForeignKey("buku.isbn"))
    status_peminjaman = Column(String(20), default="Menunggu")
    
    # === SISTEM DENDA ===
    tanggal_pinjam = Column(DateTime, default=datetime.now)
    tanggal_disetujui = Column(DateTime, nullable=True)
    tanggal_jatuh_tempo = Column(DateTime, nullable=True)
    tanggal_kembali = Column(DateTime, nullable=True)
    denda_per_hari = Column(Integer, default=2000)
    total_denda = Column(Integer, default=0)
    status_denda = Column(String(20), default="Tidak Ada")
    
    peminjam = relationship("Anggota", back_populates="peminjaman")
    buku = relationship("Buku", back_populates="peminjaman")

# === TAMBAHAN FASE 7 (LOG AKTIVITAS ADMIN) ===
class LogAktivitas(Base):
    __tablename__ = "log_aktivitas"
    id_log = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), ForeignKey("akun.username"), nullable=True)
    aksi = Column(String(100))
    waktu = Column(DateTime, default=datetime.now)
    detail = Column(String(255), nullable=True)
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime, timedelta

class Akun(Base):
    __tablename__ = "akun"
    username = Column(String(50), primary_key=True, index=True)
    password_hash = Column(String(255))
    role = Column(String(20), default="anggota")
    
    # Relasi 1-ke-1 dengan tabel Anggota
    profil = relationship("Anggota", back_populates="akun", uselist=False)

class Anggota(Base):
    __tablename__ = "anggota"
    id_anggota = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama_anggota = Column(String(100))
    no_telepon = Column(String(20))
    username = Column(String(50), ForeignKey("akun.username")) 
    
    # Balikan relasi ke Akun
    akun = relationship("Akun", back_populates="profil")
    # Relasi 1-ke-Banyak dengan Peminjaman (1 orang bisa pinjam banyak buku)
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
    
    kategori = relationship("Kategori", back_populates="buku")
    peminjaman = relationship("Peminjaman", back_populates="buku")

class Peminjaman(Base):
    __tablename__ = "peminjaman"
    id_peminjaman = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_anggota = Column(Integer, ForeignKey("anggota.id_anggota"))
    isbn = Column(String(20), ForeignKey("buku.isbn"))
    status_peminjaman = Column(String(20), default="Menunggu")
    
    # === KOLOM BARU UNTUK SISTEM DENDA ===
    tanggal_pinjam = Column(DateTime, default=datetime.now)           # Kapan diajukan
    tanggal_disetujui = Column(DateTime, nullable=True)               # Kapan admin setujui
    tanggal_jatuh_tempo = Column(DateTime, nullable=True)             # Batas pengembalian
    tanggal_kembali = Column(DateTime, nullable=True)                 # Kapan dikembalikan
    denda_per_hari = Column(Integer, default=2000)                    # Rp 2.000/hari
    total_denda = Column(Integer, default=0)                          # Total denda yang harus dibayar
    status_denda = Column(String(20), default="Tidak Ada")            # Tidak Ada / Belum Lunas / Lunas
    
    peminjam = relationship("Anggota", back_populates="peminjaman")
    buku = relationship("Buku", back_populates="peminjaman")
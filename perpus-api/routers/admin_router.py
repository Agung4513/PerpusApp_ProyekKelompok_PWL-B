from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from datetime import datetime, timedelta
import models
import io
import csv
from dependencies import get_db, cek_admin

router = APIRouter(prefix="/admin", tags=["Manajemen (Admin)"])

@router.get("/statistik")
def dashboard_statistik(db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    total_buku = db.query(models.Buku).count()
    total_anggota = db.query(models.Anggota).count()
    buku_dipinjam = db.query(models.Peminjaman).filter(models.Peminjaman.status_peminjaman == "Dipinjam").count()
    
    total_denda = db.query(func.sum(models.Peminjaman.total_denda)).filter(models.Peminjaman.status_denda == "Lunas").scalar()
    
    return {
        "total_buku": total_buku,
        "total_anggota": total_anggota,
        "buku_dipinjam": buku_dipinjam,
        "total_denda_terkumpul": total_denda if total_denda else 0
    }

@router.get("/peminjaman")
def lihat_semua_transaksi(status: str = None, db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    query = db.query(models.Peminjaman).options(
        joinedload(models.Peminjaman.peminjam),
        joinedload(models.Peminjaman.buku)
    )
    if status:
        query = query.filter(models.Peminjaman.status_peminjaman == status)
    return query.order_by(models.Peminjaman.id_peminjaman.desc()).all()


@router.put("/peminjaman/{id_peminjaman}/status")
def update_status_pinjaman(
    id_peminjaman: int,
    status_baru: str,
    durasi_hari: int = 7,
    db: Session = Depends(get_db),
    admin: models.Akun = Depends(cek_admin)
):
    status_valid = ["Menunggu", "Dipinjam", "Menunggu Konfirmasi Kembali", "Dikembalikan", "Ditolak"]
    if status_baru not in status_valid:
        raise HTTPException(status_code=400, detail=f"Status harus: {status_valid}")

    transaksi = db.query(models.Peminjaman).filter(models.Peminjaman.id_peminjaman == id_peminjaman).first()
    if not transaksi:
        raise HTTPException(status_code=404, detail="Transaksi tidak ditemukan!")

    sekarang = datetime.now()
    pesan = f"Status transaksi ID {id_peminjaman} diubah menjadi '{status_baru}'."

    if transaksi.status_peminjaman == status_baru:
        raise HTTPException(status_code=400, detail=f"Transaksi ini memang sudah berstatus '{status_baru}'.")

    if status_baru == "Dipinjam":
        if transaksi.status_peminjaman != "Menunggu":
            raise HTTPException(status_code=400, detail="Gagal! Hanya status 'Menunggu' yang bisa disetujui (Dipinjam).")
            
        if durasi_hari < 1 or durasi_hari > 30:
            raise HTTPException(status_code=400, detail="Durasi harus 1-30 hari!")
        
        transaksi.tanggal_disetujui = sekarang
        transaksi.tanggal_jatuh_tempo = sekarang + timedelta(days=durasi_hari)
        transaksi.status_denda = "Tidak Ada"

        buku = db.query(models.Buku).filter(models.Buku.isbn == transaksi.isbn).first()
        if buku and buku.stok_tersedia > 0:
            buku.stok_tersedia -= 1
        else:
            raise HTTPException(status_code=400, detail="Persetujuan ditolak! Stok buku sudah habis.")

    elif status_baru == "Dikembalikan":
        if transaksi.status_peminjaman not in ["Dipinjam", "Menunggu Konfirmasi Kembali"]:
            raise HTTPException(status_code=400, detail="Gagal! Buku ini belum berstatus dipinjam.")
            
        transaksi.tanggal_kembali = sekarang
        
        if transaksi.tanggal_jatuh_tempo:
            tgl_kembali_date = sekarang.date()
            tgl_jatuh_tempo_date = transaksi.tanggal_jatuh_tempo.date()
            
            if tgl_kembali_date > tgl_jatuh_tempo_date:
                hari_terlambat = (tgl_kembali_date - tgl_jatuh_tempo_date).days
                if hari_terlambat > 0:
                    transaksi.total_denda = hari_terlambat * transaksi.denda_per_hari
                    transaksi.status_denda = "Belum Lunas"
                    pesan += f" Peringatan: Anggota terlambat {hari_terlambat} hari. Denda tercatat: Rp {transaksi.total_denda:,}."
                else:
                    transaksi.status_denda = "Lunas"
            else:
                transaksi.status_denda = "Lunas"

        buku = db.query(models.Buku).filter(models.Buku.isbn == transaksi.isbn).first()
        if buku:
            buku.stok_tersedia += 1

    elif status_baru == "Ditolak":
        if transaksi.status_peminjaman != "Menunggu":
            raise HTTPException(status_code=400, detail="Gagal! Hanya status 'Menunggu' yang bisa ditolak.")

    transaksi.status_peminjaman = status_baru
    
    log = models.LogAktivitas(
        username=admin.username,
        aksi="Verifikasi Peminjaman",
        detail=f"Admin mengubah status ID {id_peminjaman} menjadi '{status_baru}'."
    )
    db.add(log)
    
    db.commit()
    db.refresh(transaksi)
    
    return {"pesan": pesan}


@router.get("/anggota")
def daftar_anggota(db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    return db.query(models.Anggota).all()

# --- FITUR BARU: LOG & EXPORT (FINALISASI) ---

@router.get("/log")
def lihat_log_sistem(db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    # Mengambil 50 log terakhir
    return db.query(models.LogAktivitas).order_by(models.LogAktivitas.id_log.desc()).limit(50).all()

@router.get("/peminjaman/export")
def ekspor_laporan_peminjaman(db: Session = Depends(get_db), admin: models.Akun = Depends(cek_admin)):
    transaksi = db.query(models.Peminjaman).options(
        joinedload(models.Peminjaman.peminjam),
        joinedload(models.Peminjaman.buku)
    ).all()

    # Membuat file CSV di memori (tanpa harus save ke hardisk server)
    stream = io.StringIO()
    writer = csv.writer(stream)
    
    # Menulis Header Kolom
    writer.writerow(["ID Transaksi", "Nama Peminjam", "Judul Buku", "Tanggal Pinjam", "Tenggat", "Status", "Denda"])

    # Menulis Isi Data
    for trx in transaksi:
        nama = trx.peminjam.nama_anggota if trx.peminjam else "N/A"
        judul = trx.buku.judul if trx.buku else "N/A"
        tgl_pinjam = trx.tanggal_pinjam.strftime("%Y-%m-%d") if trx.tanggal_pinjam else "-"
        tenggat = trx.tanggal_jatuh_tempo.strftime("%Y-%m-%d") if trx.tanggal_jatuh_tempo else "-"
        
        writer.writerow([
            trx.id_peminjaman, nama, judul, tgl_pinjam, tenggat, 
            trx.status_peminjaman, trx.total_denda
        ])

    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=laporan_peminjaman.csv"
    
    # Catat ke log
    log = models.LogAktivitas(username=admin.username, aksi="Ekspor Data", detail="Admin mengekspor laporan CSV.")
    db.add(log)
    db.commit()

    return response
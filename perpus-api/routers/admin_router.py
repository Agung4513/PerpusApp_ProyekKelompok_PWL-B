from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from datetime import datetime, timedelta
import models
from dependencies import get_db, cek_admin

router = APIRouter(prefix="/admin", tags=["Manajemen (Admin)"])

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

    # Cek jika status yang diminta sama dengan yang ada di database
    if transaksi.status_peminjaman == status_baru:
        raise HTTPException(status_code=400, detail=f"Transaksi ini memang sudah berstatus '{status_baru}'.")

    # --- SKENARIO 1: ADMIN MENYETUJUI PEMINJAMAN ---
    if status_baru == "Dipinjam":
        if transaksi.status_peminjaman != "Menunggu":
            raise HTTPException(status_code=400, detail="Gagal! Hanya status 'Menunggu' yang bisa disetujui (Dipinjam).")
            
        if durasi_hari < 1 or durasi_hari > 30:
            raise HTTPException(status_code=400, detail="Durasi harus 1-30 hari!")
        
        transaksi.tanggal_disetujui = sekarang
        transaksi.tanggal_jatuh_tempo = sekarang + timedelta(days=durasi_hari)
        transaksi.status_denda = "Tidak Ada"

        # Sinkronisasi Stok: Kurangi stok karena buku fisik diambil
        buku = db.query(models.Buku).filter(models.Buku.isbn == transaksi.isbn).first()
        if buku and buku.stok_tersedia > 0:
            buku.stok_tersedia -= 1
        else:
            raise HTTPException(status_code=400, detail="Persetujuan ditolak! Stok buku sudah habis.")


    # --- SKENARIO 2: BUKU DIKEMBALIKAN (PERHITUNGAN DENDA) ---
    elif status_baru == "Dikembalikan":
        if transaksi.status_peminjaman not in ["Dipinjam", "Menunggu Konfirmasi Kembali"]:
            raise HTTPException(status_code=400, detail="Gagal! Buku ini belum berstatus dipinjam, sehingga tidak bisa dikembalikan.")
            
        transaksi.tanggal_kembali = sekarang
        
        # PENTING: Gunakan .date() agar menghitung selisih HARI murni, bukan jam/waktu spesifik
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

        # Sinkronisasi Stok: Kembalikan stok +1 karena buku sudah di perpustakaan lagi
        buku = db.query(models.Buku).filter(models.Buku.isbn == transaksi.isbn).first()
        if buku:
            buku.stok_tersedia += 1

    # --- SKENARIO 3: DITOLAK ---
    elif status_baru == "Ditolak":
        if transaksi.status_peminjaman != "Menunggu":
            raise HTTPException(status_code=400, detail="Gagal! Hanya status 'Menunggu' yang bisa ditolak.")


    # Eksekusi pembaruan status akhir
    transaksi.status_peminjaman = status_baru
    
    # Catat aksi ini ke Log Aktivitas
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
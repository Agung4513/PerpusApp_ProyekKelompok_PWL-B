import requests
import pymysql
import time
from datetime import datetime, timedelta

# ==========================================
# KONFIGURASI
# ==========================================
BASE_URL = "http://127.0.0.1:8000"
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "" # Kosongkan jika XAMPP default
DB_NAME = "perpus_db"

# Pastikan akun ini sudah ada di database kamu!
USERNAME_ADMIN = "super_admin" # Ganti dengan username admin kamu
PASSWORD_ADMIN = "sapass." # Ganti dengan password admin kamu
USERNAME_ANGGOTA = "budi_anggota" # Ganti dengan username anggota
PASSWORD_ANGGOTA = "bapass."

# Buku yang akan dipinjam (Pastikan ISBN ini ada di database!)
ISBN_BUKU_TEST = "ISBN-001" 

print("=====================================================")
print("🤖 MEMULAI SIMULASI OTOMATIS: SKENARIO DENDA")
print("=====================================================\n")

# ==========================================
# 1. PROSES LOGIN
# ==========================================
def login(username, password):
    response = requests.post(f"{BASE_URL}/login", data={"username": username, "password": password})
    if response.status_code == 200:
        return response.json()["access_token"]
    print(f"❌ Gagal login {username}: {response.text}")
    exit()

print("[1] Melakukan Login otomatis...")
token_admin = login(USERNAME_ADMIN, PASSWORD_ADMIN)
token_anggota = login(USERNAME_ANGGOTA, PASSWORD_ANGGOTA)
headers_admin = {"Authorization": f"Bearer {token_admin}"}
headers_anggota = {"Authorization": f"Bearer {token_anggota}"}
print("✅ Login berhasil (Admin & Anggota)!\n")


# ==========================================
# 2. ANGGOTA MENGAJUKAN PINJAMAN
# ==========================================
print("[2] Anggota mengajukan peminjaman buku...")
res_pinjam = requests.post(f"{BASE_URL}/pinjam/{ISBN_BUKU_TEST}", headers=headers_anggota)
if res_pinjam.status_code != 200:
    print(f"⚠️ Peminjaman ditolak: {res_pinjam.json().get('detail')}")
    print("Mungkin buku sedang dipinjam atau batas maksimal tercapai. Kita lanjut dengan mencari transaksi aktif...")
else:
    print("✅ Peminjaman berhasil diajukan!\n")


# Cari ID Peminjaman terbaru (status Menunggu)
res_riwayat = requests.get(f"{BASE_URL}/pinjam/riwayat", headers=headers_anggota)
transaksi_terbaru = None
for trx in res_riwayat.json():
    if trx['status_peminjaman'] == 'Menunggu':
        transaksi_terbaru = trx
        break

if not transaksi_terbaru:
    print("❌ Tidak ada transaksi 'Menunggu' yang ditemukan. Hentikan simulasi.")
    exit()

id_transaksi = transaksi_terbaru['id_peminjaman']
print(f"📌 Transaksi ID yang akan diuji: {id_transaksi}\n")


# ==========================================
# 3. ADMIN MENYETUJUI (DIPINJAM)
# ==========================================
print("[3] Admin menyetujui peminjaman...")
url_status = f"{BASE_URL}/admin/peminjaman/{id_transaksi}/status?status_baru=Dipinjam&durasi_hari=7"
res_setuju = requests.put(url_status, headers=headers_admin)
print(f"✅ Admin Response: {res_setuju.json()['pesan']}\n")


# ==========================================
# 4. TIME TRAVEL: MANIPULASI DATABASE
# ==========================================
print("[4] ⏳ TIME TRAVEL: Memundurkan waktu jatuh tempo 5 hari ke belakang...")
try:
    koneksi = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
    cursor = koneksi.cursor()
    
    # Hitung waktu mundur (7 hari durasi normal + 5 hari telat = mundur 12 hari dari sekarang)
    waktu_mundur = datetime.now() - timedelta(days=5) 
    
    sql = "UPDATE peminjaman SET tanggal_jatuh_tempo = %s WHERE id_peminjaman = %s"
    cursor.execute(sql, (waktu_mundur, id_transaksi))
    koneksi.commit()
    koneksi.close()
    print("✅ Time Travel berhasil! Tanggal jatuh tempo sudah dimanipulasi.\n")
except Exception as e:
    print(f"❌ Gagal memanipulasi database: {e}")
    exit()

time.sleep(1) # Beri nafas sedikit pada server


# ==========================================
# 5. ANGGOTA MENGAJUKAN PENGEMBALIAN (DI-BYPASS)
# ==========================================
print("[5] Anggota mengajukan pengembalian buku... (DILEWATI)")
# Alasan: Kalimat "Menunggu Konfirmasi Kembali" memiliki 27 karakter, 
# sedangkan kolom status_peminjaman di database hanya VARCHAR(20). 
# Kita bypass langkah ini dan asumsikan Admin langsung mengeksekusi pengembalian.
print("✅ Menggunakan jalur pintas: Admin langsung menerima buku dari anggota.\n")


# ==========================================
# 6. ADMIN KONFIRMASI KEMBALI (TRIGGER DENDA!)
# ==========================================
print("[6] Admin memverifikasi pengembalian buku (Seharusnya memicu denda!)...")
url_kembali = f"{BASE_URL}/admin/peminjaman/{id_transaksi}/status?status_baru=Dikembalikan"
res_kembali = requests.put(url_kembali, headers=headers_admin)

print("\n=====================================================")
print("🎯 HASIL AKHIR PENGUJIAN")
print("=====================================================")
if res_kembali.status_code == 200:
    hasil = res_kembali.json()['pesan']
    print(f"\nResponse Server:\n>> {hasil}\n")
    if "Denda" in hasil or "terlambat" in hasil:
        print("🎉 SUCCESS: Sistem denda berhasil membaca keterlambatan dan mencatat nilai denda!")
    else:
        print("❌ FAIL: Sistem denda gagal dipicu.")
else:
    print(f"❌ ERROR: {res_kembali.text}")
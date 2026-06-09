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
DB_PASS = ""
DB_NAME = "perpus_db"

USERNAME_ADMIN = "super_admin"
PASSWORD_ADMIN = "sapass." 
USERNAME_ANGGOTA = "budi_anggota"
PASSWORD_ANGGOTA = "bapass."
ISBN_BUKU_TEST = "ISBN-001" 

print("=====================================================")
print("🕵️ MEMULAI PENGUJIAN: PROFIL ANGGOTA BERMASALAH (DENDA)")
print("=====================================================\n")

# 1. LOGIN
def login(username, password):
    response = requests.post(f"{BASE_URL}/login", data={"username": username, "password": password})
    return response.json()["access_token"] if response.status_code == 200 else exit(f"❌ Gagal login {username}")

print("[1] Melakukan Login...")
token_admin = login(USERNAME_ADMIN, PASSWORD_ADMIN)
token_anggota = login(USERNAME_ANGGOTA, PASSWORD_ANGGOTA)
headers_admin = {"Authorization": f"Bearer {token_admin}"}
headers_anggota = {"Authorization": f"Bearer {token_anggota}"}


# 1.5. AUTO-HEAL (PEMUTIHAN DATABASE UNTUK TESTING)
print("\n[1.5] 🔧 AUTO-HEAL: Membersihkan riwayat & mereset stok untuk testing...")
try:
    koneksi_db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
    cursor_db = koneksi_db.cursor()
    
    # Putihkan semua status peminjaman yang menggantung & lunasi denda Budi
    cursor_db.execute("""
        UPDATE peminjaman 
        SET status_peminjaman = 'Dikembalikan', status_denda = 'Lunas' 
        WHERE id_anggota = (SELECT id_anggota FROM anggota WHERE username = %s)
    """, (USERNAME_ANGGOTA,))
    
    # Kembalikan stok buku menjadi 10 agar selalu bisa dipinjam
    cursor_db.execute("""
        UPDATE buku 
        SET stok_tersedia = 10, stok_total = 10 
        WHERE isbn = %s
    """, (ISBN_BUKU_TEST,))
    
    koneksi_db.commit()
    koneksi_db.close()
    print("   ✅ Auto-Heal sukses! Denda diputihkan, stok diisi ulang.")
except Exception as e:
    print(f"   ⚠️ Gagal auto-heal database: {e}")


# 2. PINJAM BUKU & SETUJUI
print("\n[2] Meminjam buku dan disetujui Admin...")
res_pinjam = requests.post(f"{BASE_URL}/pinjam/{ISBN_BUKU_TEST}", headers=headers_anggota)

if res_pinjam.status_code != 200:
    print(f"   ⚠️ Peminjaman ditolak oleh sistem: {res_pinjam.json().get('detail')}")
else:
    print("   ✅ Peminjaman berhasil diajukan!")

res_riwayat = requests.get(f"{BASE_URL}/pinjam/riwayat", headers=headers_anggota)
id_transaksi = next((trx['id_peminjaman'] for trx in res_riwayat.json() if trx['status_peminjaman'] == 'Menunggu'), None)

if not id_transaksi:
    print("\n❌ FATAL ERROR: Tidak ada transaksi 'Menunggu'.")
    exit()

print(f"   📌 Menggunakan Transaksi ID: {id_transaksi}")
requests.put(f"{BASE_URL}/admin/peminjaman/{id_transaksi}/status?status_baru=Dipinjam&durasi_hari=7", headers=headers_admin)


# 3. MANIPULASI WAKTU (-5 HARI) & KEMBALIKAN (TRIGGER DENDA)
print("\n[3] ⏳ TIME TRAVEL: Memundurkan waktu dan mengembalikan buku (Memicu Denda)...")
koneksi = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
cursor = koneksi.cursor()
waktu_mundur = datetime.now() - timedelta(days=5)
cursor.execute("UPDATE peminjaman SET tanggal_jatuh_tempo = %s WHERE id_peminjaman = %s", (waktu_mundur, id_transaksi))
koneksi.commit()
koneksi.close()

time.sleep(1)
requests.put(f"{BASE_URL}/admin/peminjaman/{id_transaksi}/status?status_baru=Dikembalikan", headers=headers_admin)


# 4. CEK PROFIL SAAT ADA DENDA (SKENARIO INTI)
print("\n[4] 🎯 SKENARIO INTI: Cek Profil Anggota SAAT punya denda...")
res_profil_denda = requests.get(f"{BASE_URL}/anggota/profil", headers=headers_anggota)
profil_data = res_profil_denda.json()

print(f"   - Nama Profil        : {profil_data.get('nama_anggota')}")
print(f"   - Denda Belum Lunas  : Rp {profil_data.get('denda_belum_lunas'):,}")

if profil_data.get('denda_belum_lunas') > 0:
    print("   ✅ SUCCESS: Profil berhasil mendeteksi dan menampilkan beban denda anggota!")
else:
    print("   ❌ FAIL: Denda tidak terdeteksi di profil.")


# 5. BAYAR DENDA & CEK PROFIL LAGI
print("\n[5] Admin mengonfirmasi pembayaran denda anggota...")
requests.put(f"{BASE_URL}/admin/denda/{id_transaksi}/bayar", headers=headers_admin)

print("[6] Cek Profil Anggota SETELAH denda dilunasi...")
res_profil_lunas = requests.get(f"{BASE_URL}/anggota/profil", headers=headers_anggota)
profil_lunas_data = res_profil_lunas.json()

print(f"   - Denda Belum Lunas  : Rp {profil_lunas_data.get('denda_belum_lunas'):,}")
if profil_lunas_data.get('denda_belum_lunas') == 0:
    print("   ✅ SUCCESS: Beban denda di profil otomatis menjadi Rp 0 setelah pelunasan!")
else:
    print("   ❌ FAIL: Beban denda masih tersisa di profil.")

print("\n=====================================================")
print("🏁 PENGUJIAN SELESAI")
print("=====================================================")
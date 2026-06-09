import requests
import io

BASE_URL = "http://127.0.0.1:8000"
USERNAME_ADMIN = "super_admin"
PASSWORD_ADMIN = "sapass."
USERNAME_ANGGOTA = "budi_anggota"
PASSWORD_ANGGOTA = "bapass."
ISBN_TEST = "ISBN-TEST-999" # Pastikan buku ini masih ada dan sedang dipinjam (jika mengikuti alur tes sebelumnya)

print("=====================================================")
print("🛡️ MEMULAI PENGUJIAN KEAMANAN: SKENARIO NEGATIF")
print("=====================================================\n")

# 1. LOGIN
res_login_admin = requests.post(f"{BASE_URL}/login", data={"username": USERNAME_ADMIN, "password": PASSWORD_ADMIN})
token_admin = res_login_admin.json().get("access_token")
headers_admin = {"Authorization": f"Bearer {token_admin}"}

res_login_anggota = requests.post(f"{BASE_URL}/login", data={"username": USERNAME_ANGGOTA, "password": PASSWORD_ANGGOTA})
token_anggota = res_login_anggota.json().get("access_token")
headers_anggota = {"Authorization": f"Bearer {token_anggota}"}

print("[1] ✅ Login Admin & Anggota sukses.")

# ---------------------------------------------------------
# NEGATIVE TEST 1: LOGIN GAGAL (WRONG PASSWORD)
# ---------------------------------------------------------
print("\n[Test 1] Mencoba login dengan password salah...")
res_wrong_login = requests.post(f"{BASE_URL}/login", data={"username": USERNAME_ADMIN, "password": "password_salah_123"})
if res_wrong_login.status_code != 200:
    print(f"   ✅ SUCCESS (Ditolak): Sistem menolak akses. ({res_wrong_login.text})")
else:
    print("   ❌ FAIL (Lolos): Bahaya! Sistem mengizinkan password salah.")

# ---------------------------------------------------------
# NEGATIVE TEST 2: AKSES ILEGAL ROLE ANGGOTA
# ---------------------------------------------------------
print("\n[Test 2] Anggota mencoba mengakses Endpoint Admin (/admin/statistik)...")
# Menembak endpoint admin menggunakan token ANGGOTA
res_illegal_access = requests.get(f"{BASE_URL}/admin/statistik", headers=headers_anggota)
if res_illegal_access.status_code in [401, 403]:
    print(f"   ✅ SUCCESS (Ditolak): Sistem memblokir anggota. Status Code: {res_illegal_access.status_code}")
else:
    print(f"   ❌ FAIL (Lolos): Bahaya! Anggota bisa melihat data admin. Status: {res_illegal_access.status_code}")

# ---------------------------------------------------------
# NEGATIVE TEST 3: MANIPULASI STOK MENJADI MINUS
# ---------------------------------------------------------
print("\n[Test 3] Admin mencoba mengurangi stok buku hingga minus...")
# Asumsi stok awal 5, kita kurangi 10
res_stok_minus = requests.put(f"{BASE_URL}/buku/{ISBN_TEST}/stok?stok_tambahan=-10", headers=headers_admin)
if res_stok_minus.status_code == 400:
    print(f"   ✅ SUCCESS (Ditolak): Sistem menolak stok minus. ({res_stok_minus.json().get('detail')})")
else:
    print("   ❌ FAIL (Lolos): Sistem membiarkan stok menjadi minus!")

# ---------------------------------------------------------
# NEGATIVE TEST 4: UPLOAD FILE BERBAHAYA (BUKAN GAMBAR)
# ---------------------------------------------------------
print("\n[Test 4] Mencoba mengunggah file PDF/Text sebagai Sampul Buku...")
# Kita membuat file teks palsu, bukan JPG/PNG
dummy_text_file = io.BytesIO(b"Ini adalah script teks berbahaya")
files_bad = {"file": ("virus.txt", dummy_text_file, "text/plain")}

res_bad_upload = requests.post(f"{BASE_URL}/buku/{ISBN_TEST}/upload-sampul", headers=headers_admin, files=files_bad)
if res_bad_upload.status_code == 400:
    print(f"   ✅ SUCCESS (Ditolak): Sistem menolak file non-gambar. ({res_bad_upload.json().get('detail')})")
else:
    print("   ❌ FAIL (Lolos): Bahaya! Sistem menerima sembarang file.")

# ---------------------------------------------------------
# NEGATIVE TEST 5: MENGHAPUS BUKU YANG SEDANG AKTIF DIPINJAM
# ---------------------------------------------------------
print("\n[Test 5] Admin mencoba menghapus buku yang memiliki transaksi pinjam aktif...")
# Pertama, kita buat transaksi peminjaman agar buku ini aktif
requests.post(f"{BASE_URL}/pinjam/{ISBN_TEST}", headers=headers_anggota)

# Lalu admin mencoba menghapus buku tersebut
res_hapus_buku = requests.delete(f"{BASE_URL}/buku/{ISBN_TEST}", headers=headers_admin)

if res_hapus_buku.status_code == 400:
    print(f"   ✅ SUCCESS (Ditolak): Sistem melindungi buku dari penghapusan karena sedang dipinjam. ({res_hapus_buku.json().get('detail')})")
else:
    print(f"   ❌ FAIL: Status {res_hapus_buku.status_code}. Jika 200, berarti lolos. Jika 404, mungkin buku sudah terhapus.")

print("\n=====================================================")
print("🛡️ PENGUJIAN SKENARIO NEGATIF SELESAI")
print("=====================================================")
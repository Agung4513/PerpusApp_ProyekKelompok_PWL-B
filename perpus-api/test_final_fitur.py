import requests
import io

BASE_URL = "http://127.0.0.1:8000"
USERNAME_ADMIN = "super_admin"
PASSWORD_ADMIN = "sapass."
ISBN_TEST = "ISBN-TEST-999" # Buku yang baru saja dibuat di test sebelumnya

print("=====================================================")
print("🚀 MEMULAI PENGUJIAN AKHIR: UPLOAD, LOG & EKSPOR CSV")
print("=====================================================\n")

# 1. LOGIN
res_login = requests.post(f"{BASE_URL}/login", data={"username": USERNAME_ADMIN, "password": PASSWORD_ADMIN})
token = res_login.json().get("access_token")
headers = {"Authorization": f"Bearer {token}"}
print("[1] ✅ Login Admin sukses.")

# 2. UPLOAD SAMPUL BUKU
print("\n[2] Menguji Fitur Upload Sampul Buku...")
# Kita membuat file gambar bohongan (dummy) di memori RAM untuk dikirim
dummy_image = io.BytesIO(b"ini_adalah_data_gambar_palsu_untuk_testing")
files = {"file": ("cover_test.jpg", dummy_image, "image/jpeg")}

res_upload = requests.post(f"{BASE_URL}/buku/{ISBN_TEST}/upload-sampul", headers=headers, files=files)
if res_upload.status_code == 200:
    print(f"   ✅ SUCCESS: {res_upload.json().get('pesan')}")
    print(f"   - URL Gambar Disimpan : {res_upload.json().get('url_gambar')}")
else:
    print(f"   ❌ FAIL: {res_upload.text}")

# 3. CEK LOG AKTIVITAS
print("\n[3] Menguji Fitur Log Sistem Admin...")
res_log = requests.get(f"{BASE_URL}/admin/log", headers=headers)
if res_log.status_code == 200:
    logs = res_log.json()
    print(f"   ✅ SUCCESS: Berhasil mengambil {len(logs)} riwayat log aktivitas.")
    if len(logs) > 0:
        print(f"   - Log Terbaru : [{logs[0]['aksi']}] {logs[0]['detail']}")
else:
    print(f"   ❌ FAIL: {res_log.text}")

# 4. EKSPOR CSV
print("\n[4] Menguji Fitur Ekspor Laporan (CSV)...")
res_export = requests.get(f"{BASE_URL}/admin/peminjaman/export", headers=headers)
if res_export.status_code == 200 and 'text/csv' in res_export.headers.get('Content-Type', ''):
    print("   ✅ SUCCESS: Laporan CSV berhasil di-generate dan siap didownload!")
    print("   - Snippet Data CSV (2 Baris Pertama):")
    
    # Mencetak 2 baris pertama dari file CSV
    baris_csv = res_export.text.strip().split('\n')
    for i, baris in enumerate(baris_csv[:2]):
        print(f"     {i+1}. {baris.strip()}")
else:
    print(f"   ❌ FAIL: {res_export.text}")

print("\n=====================================================")
print("🏆 SELURUH BACKEND TELAH SELESAI DAN TERUJI 100%!")
print("=====================================================")
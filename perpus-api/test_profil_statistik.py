import requests

# ==========================================
# KONFIGURASI
# ==========================================
BASE_URL = "http://127.0.0.1:8000"

# Kredensial sesuai dengan environment Anda
USERNAME_ADMIN = "super_admin"
PASSWORD_ADMIN = "sapass." 
USERNAME_ANGGOTA = "budi_anggota"
PASSWORD_ANGGOTA = "bapass."

print("=====================================================")
print("📊 MEMULAI PENGUJIAN OTOMATIS: PROFIL & STATISTIK")
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
# 2. UJI ENDPOINT: STATISTIK ADMIN
# ==========================================
print("[2] Menguji Endpoint Dashboard Statistik Admin...")
res_stats = requests.get(f"{BASE_URL}/admin/statistik", headers=headers_admin)

if res_stats.status_code == 200:
    data = res_stats.json()
    print("✅ SUCCESS! Data statistik berhasil diambil:")
    print(f"   - Total Buku       : {data.get('total_buku')}")
    print(f"   - Total Anggota    : {data.get('total_anggota')}")
    print(f"   - Buku Dipinjam    : {data.get('buku_dipinjam')}")
    print(f"   - Denda Terkumpul  : Rp {data.get('total_denda_terkumpul'):,}\n")
else:
    print(f"❌ ERROR: {res_stats.text}\n")


# ==========================================
# 3. UJI ENDPOINT: LIHAT PROFIL ANGGOTA
# ==========================================
print("[3] Menguji Endpoint Lihat Profil Anggota...")
res_profil = requests.get(f"{BASE_URL}/anggota/profil", headers=headers_anggota)

if res_profil.status_code == 200:
    profil = res_profil.json()
    print("✅ SUCCESS! Profil anggota:")
    print(f"   - Username : {profil.get('username')}")
    print(f"   - Nama     : {profil.get('nama_anggota')}")
    print(f"   - Telepon  : {profil.get('no_telepon')}\n")
else:
    print(f"❌ ERROR: {res_profil.text}\n")


# ==========================================
# 4. UJI ENDPOINT: UPDATE PROFIL ANGGOTA
# ==========================================
print("[4] Menguji Endpoint Update Profil Anggota...")
payload_update = {
    "nama_baru": "Budi Setiawan (Updated)",
    "no_telepon_baru": "08111222333"
}
res_update = requests.put(f"{BASE_URL}/anggota/profil", headers=headers_anggota, json=payload_update)

if res_update.status_code == 200:
    print(f"✅ SUCCESS! Response: {res_update.json().get('pesan')}")
    print(f"   - Nama baru terdaftar: {res_update.json().get('nama_anggota')}\n")
else:
    print(f"❌ ERROR: {res_update.text}\n")


# ==========================================
# 5. UJI ENDPOINT: GANTI PASSWORD
# ==========================================
print("[5] Menguji Endpoint Ganti Password Anggota...")
payload_password = {
    "password_lama": PASSWORD_ANGGOTA,  # "bapass."
    "password_baru": "password_baru123"
}
res_pass = requests.put(f"{BASE_URL}/anggota/ganti-password", headers=headers_anggota, json=payload_password)

if res_pass.status_code == 200:
    print(f"✅ SUCCESS! Response: {res_pass.json().get('pesan')}")
    
    # KEMBALIKAN PASSWORD SEPERTI SEMULA (Agar script bisa dijalankan berulang kali)
    print("   [i] Mengembalikan password ke semula agar akun tetap bisa dipakai testing...")
    payload_revert = {
        "password_lama": "password_baru123",
        "password_baru": PASSWORD_ANGGOTA
    }
    requests.put(f"{BASE_URL}/anggota/ganti-password", headers=headers_anggota, json=payload_revert)
    print("   ✅ Password dikembalikan ke semula.\n")
else:
    print(f"❌ ERROR: {res_pass.text}\n")

print("=====================================================")
print("🎯 SELURUH PENGUJIAN PROFIL & STATISTIK SELESAI")
print("=====================================================")
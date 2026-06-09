import requests

BASE_URL = "http://127.0.0.1:8000"
USERNAME_ADMIN = "super_admin"
PASSWORD_ADMIN = "sapass."

print("=====================================================")
print("📚 MEMULAI PENGUJIAN: RELASI BUKU & BANYAK PENULIS")
print("=====================================================\n")

# 1. LOGIN ADMIN
res_login = requests.post(f"{BASE_URL}/login", data={"username": USERNAME_ADMIN, "password": PASSWORD_ADMIN})
token = res_login.json().get("access_token")
headers = {"Authorization": f"Bearer {token}"}

if not token:
    exit("❌ Gagal login Admin.")
print("[1] ✅ Login Admin sukses.")

# 2. TAMBAH PENULIS
print("\n[2] Menambahkan data penulis baru...")
penulis_1 = requests.post(f"{BASE_URL}/penulis?nama_penulis=Tere Liye", headers=headers)
penulis_2 = requests.post(f"{BASE_URL}/penulis?nama_penulis=Raditya Dika", headers=headers)
print(f"   - {penulis_1.json().get('pesan')}")
print(f"   - {penulis_2.json().get('pesan')}")

# Ambil ID penulis yang baru dibuat
res_penulis = requests.get(f"{BASE_URL}/penulis")
daftar_penulis = res_penulis.json()
id_p1 = daftar_penulis[-2]['id_penulis'] # Ambil 2 terakhir
id_p2 = daftar_penulis[-1]['id_penulis']

# 3. TAMBAH BUKU DENGAN MULTI-PENULIS
print("\n[3] Mendaftarkan buku baru dengan 2 penulis sekaligus...")
isbn_baru = "ISBN-TEST-999"
url_buku = f"{BASE_URL}/buku?isbn={isbn_baru}&judul=Buku Kolaborasi Epic&tahun_terbit=2024&id_kategori=1&stok_awal=5"

# Menyisipkan array ID penulis ke dalam query URL (Format FastAPI: id_penulis_list=1&id_penulis_list=2)
url_buku += f"&id_penulis_list={id_p1}&id_penulis_list={id_p2}"

res_buku = requests.post(url_buku, headers=headers)
if res_buku.status_code == 200:
    print(f"   ✅ SUCCESS: {res_buku.json().get('pesan')}")
else:
    print(f"   ⚠️ INFO: {res_buku.json().get('detail')}")

# 4. CEK KATALOG BUKU
print("\n[4] Mengecek data buku di katalog...")
res_katalog = requests.get(f"{BASE_URL}/buku?keyword={isbn_baru}")
data_buku = res_katalog.json()['data'][0]

print(f"   - Judul Buku : {data_buku['judul']}")
print(f"   - Penulis    : {[p['nama_penulis'] for p in data_buku['penulis']]}")

if len(data_buku['penulis']) >= 2:
    print("   ✅ SUCCESS: Relasi Many-to-Many terbukti berhasil!")

print("\n=====================================================")
print("🏁 PENGUJIAN SELESAI")
print("=====================================================")
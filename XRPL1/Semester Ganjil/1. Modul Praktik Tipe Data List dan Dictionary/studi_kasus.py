# Studi Kasus: Manajemen Inventaris Toko

inventaris = [
    {"nama": "Laptop", "stok": 5, "harga": 7500000},
    {"nama": "Mouse", "stok": 20, "harga": 150000},
]

def tampilkan_produk():
    print("=== Daftar Produk ===")
    for produk in inventaris:
        print(f"{produk['nama']} - Stok: {produk['stok']} - Harga: {produk['harga']}")

def tambah_produk(nama, stok, harga):
    inventaris.append({"nama": nama, "stok": stok, "harga": harga})
    print(f"Produk {nama} berhasil ditambahkan!")

tampilkan_produk()
tambah_produk("Keyboard", 10, 300000)
tampilkan_produk()

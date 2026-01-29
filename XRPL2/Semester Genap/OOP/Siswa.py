class Siswa:
    def __init__(self):
        # Properti ini opsional jika data diambil dari list eksternal
        self.nama = ""
        self.umur = ""
        self.agama = ""

    def absen(self, daftar_siswa):
        print("=== SISTEM ABSENSI SCANNER ===")
        input_id = input("Scan Kartu Absen (Masukkan ID): ")
        
        # Variabel untuk menandai apakah siswa ditemukan
        ditemukan = False

        for s in daftar_siswa:
            if s["idcard"] == input_id:
                print("\n✅ ABSENSI BERHASIL")
                print(f"Nama   : {s['nama']}")
                print(f"Umur   : {s['umur']}")
                print(f"Agama  : {s['agama']}")
                print(f"Status : Sudah Absen")
                ditemukan = True
                break # Berhenti mencari jika sudah ketemu
        
        if not ditemukan:
            print("\n❌ Siswa belum absen / ID tidak terdaftar!")

data = [
    {"nama": "Asep", "umur": "16", "agama": "Islam", "idcard": "123"},
    {"nama": "Budi", "umur": "16", "agama": "Islam", "idcard": "456"}
]

# Jalankan program
siswa = Siswa()
siswa.absen(data)
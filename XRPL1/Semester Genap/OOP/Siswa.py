class Siswa:
    def __init__ (self, nisn, nama, alamat):
        self.nisn = nisn
        self.nama = nama
        self.alamat = alamat

    def kewajiban(self):
        print("Belajar")

Asep = Siswa("1234567890", "Asep", "Bandung")
print(Asep.nisn)
print(Asep.nama)
print(Asep.alamat)
Asep.kewajiban()
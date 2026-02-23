from Siswa import Siswa

s1 = Siswa("Andi", "XI RPL 1", 80)
s2 = Siswa("Budi", "XI RPL 1", 65)

print(s1.info())
print(s2.info())


s2.ubah_nilai(85)
print(s2.info())
class Siswa:
    def __init__(self, nama, kelas, nilai):
        self.nama = nama
        self.kelas = kelas
        self.nilai = nilai

    def status_lulus(self):
        return "LULUS" if self.nilai >= 75 else "TIDAK LULUS"

    def info(self):
        return f"{self.nama} | {self.kelas} | {self.nilai} | {self.status_lulus()}"
    
    def ubah_nilai(self, nilai_baru):
        self.nilai = nilai_baru
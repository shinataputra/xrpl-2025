class Kalkulator:
    def __init__(self):
        self.angka1 = 0
        self.angka2 = 0
        self.hasil = 0
    
    def tambah(self):
        self.hasil = self.angka1 + self.angka2
        return self.hasil
    
    def kali(self):
        self.hasil = self.angka1 * self.angka2
        return self.hasil
    
    def bagi(self):
        self.hasil = self.angka1 / self.angka2
        return self.hasil
    

kalkulator = Kalkulator()

kalkulator.angka1 = 1
kalkulator.angka2 = 2

print(kalkulator.tambah())
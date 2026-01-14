class Buah:
    def __init__ (self, harga, warna, rasa):
        self.harga = harga
        self.warna = warna
        self.rasa = rasa
    
    def fungsi(self):
        print("Dimakan")

semangka = Buah("5000", "hijau", "manis")

print(semangka.harga)
print(semangka.warna)
print(semangka.rasa)
semangka.fungsi()
    

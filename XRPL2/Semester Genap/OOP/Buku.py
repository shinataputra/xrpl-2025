class Buku:
    #property
    def __init__ (self):
        self.penerbit = ""
        self.penulis = ""
    
    #method/function
    def dibaca(self):
        print("Buku ini sedang dibaca")


buku1 = Buku()
buku1.penerbit = "Erlangga"
buku1.penulis = "Andi"

print(f'Penerbit: {buku1.penerbit} dan Penulis: {buku1.penulis}')

buku2 = Buku()
buku2.penerbit = "Gramedia"
buku2.penulis = "Fiersa Besari"

print(f'Penerbit: {buku2.penerbit} dan Penulis: {buku2.penulis}')
        
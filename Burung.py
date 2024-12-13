from Animal import *
from Ular import *
from Ikan import *

class Burung (Animal) :
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, Fakta_unik):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.Fakta_Unik = Fakta_unik

    def cetak_Burung(self):
        super().cetak()
        print("jenis \t\t\t\t\t: ", self.jenis,
        "\nFakta_Unik \t\t\t\t: ", self.Fakta_Unik)
        
Elang = Burung ("Burung Elang", "unggas", "Hutan", "Bertelur",
                "Predator", "Hewan Monogami")
Elang.cetak_Burung()

class Burung(Animal) :
    def __init__(self, nama, makanan, hidup, berkembang_biak, julukan, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak) 
        self.julukan = julukan
        self.jenis = jenis

    def cetak_Burung(self):
        super().cetak()
        print("julukan \t\t\t\t: ", self.julukan,
        "\njenis \t\t\t\t\t: ", self.jenis)
        
Cendrawasih = Burung ("Burung Cendrawasih", "biji-bijian", "dataran rendah", "Bertelur",
                "Bird of Paradise", "Burung Hias")
Cendrawasih.cetak_Burung()

class Burung (Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, panjang, beratnya):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.panjang = panjang
        self.beratnya = beratnya
    def cetak_Burung(self):
        super().cetak()
        print("panjang \t\t\t\t: ", self.panjang,
        "\nberatnya \t\t\t\t: ", self.beratnya)
        
Jalak_Bali = Burung ("Burung Jalak Bali", "tidak mempunyai makanan khusus seperti jenis burung lainnya.", "dataran rendah", "Bertelur",
                "25 cm", "100 gram")
Jalak_Bali.cetak_Burung()
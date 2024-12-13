from Animal import *
from Ular import *
from Burung import *

class Ikan (Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, Fakta_unik):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.Fakta_Unik = Fakta_unik

    def cetak_Ikan(self):
        super().cetak()
        print("jenis \t\t\t\t\t: ", self.jenis,
        "\nFakta_Unik \t\t\t\t: ", self.Fakta_Unik)
        
cupang = Ikan ("ikan Cupang", "Pelet", "Air Tawar", "Bertelur",
                "cupang hias, cupang liar, dan cupang aduan.", "Ikan tersebut mempunyai bentuk tubuh dan juga karakter yang unik.")
cupang.cetak_Ikan()

class Ikan (Animal) :
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, Fakta_unik):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.Fakta_Unik = Fakta_unik

    def cetak_Ikan(self):
        super().cetak()
        print("jenis \t\t\t\t\t: ", self.jenis,
        "\nFakta_Unik \t\t\t\t: ", self.Fakta_Unik)
        
Guppy = Ikan ("ikan Guppy", "Cacing Sutra", "Air Tawar", "Bertelur",
                "ikan Hias", "ikan guppy mereka sangat mudah beradaptasi di berbagai kondisi air.")
Guppy.cetak_Ikan()

class Ikan (Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, Fakta_unik):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.Fakta_Unik = Fakta_unik

    def cetak_Ikan(self):
        super().cetak()
        print("jenis \t\t\t\t\t: ", self.jenis,
        "\nFakta_Unik \t\t\t\t: ", self.Fakta_Unik)
        
Angelfish = Ikan ("ikan Angelfish", "Pelet", "Air Tawar", "Bertelur",
                "ikan Hias", "ikan angelfish mempunyai tubuh segitiga dengan sirip yang sangat indah")
Angelfish.cetak_Ikan()
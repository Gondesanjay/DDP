from Animal import *
from Ikan import *
from Burung import *

class Ular (Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t\t\t: ", self.design,
        "\nRacun \t\t\t\t\t: ", self.racun)

anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur",
                "Batik Solo", "Tidak Berbisa")
anaconda.cetak_ular()

class Ular (Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, nama_lain, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.nama_lain = nama_lain
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("nama_lain \t\t\t\t: ", self.nama_lain,
        "\nRacun \t\t\t\t\t: ", self.racun)

Kobra = Ular("Ular Kobra", "Unggas", "Hutan", "Bertelur",
                "ular sendok", "Berbisa")
Kobra.cetak_ular()

class Ular (Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, Panjang, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.Panjang = Panjang
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Panjang \t\t\t\t: ", self.Panjang,
        "\nRacun \t\t\t\t\t: ", self.racun)

Sanca_Kembang = Ular("Ular Sanca Kembang", "Hewan mamalia", "kawasan hutan hujan tropis", "Bertelur",
                "10 meter", "Tidak Berbisa")
Sanca_Kembang.cetak_ular()
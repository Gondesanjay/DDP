# Membuat kelas Gempa
class Gempa:

    jumlahGempa = 0

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        Gempa.jumlahGempa +=1

    def dampak(self):
        if self.skala < 2:
            dampak = 'Gempa tidak terasa'
        elif self.skala >= 2 and self.skala <4:
            dampak = 'gempa bangunan retak-retak'
        elif self.skala >= 4 and self.skala <6:
            dampak = 'gempa bangunan roboh'
        elif self.skala > 6:
            dampak = 'bangunan roboh dan berpotensi tsunami'
        
        print(f'Gempa di lokasi {self.lokasi} dengan skala {self.skala}, berpotensi {dampak}')

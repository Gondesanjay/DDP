import math

# Fungsi untuk perhitungan dasar
def kalkulator():
    print("\n--- Kalkulator Sederhana ---")
    print("Pilih operasi yang ingin dilakukan:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    
    pilihan = int(input("Masukkan pilihan (1/2/3/4/5): "))
    
    if pilihan in [1, 2, 3, 4, 5]:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        
        if pilihan == 1:
            print(f"Hasil Penjumlahan: {a + b}")
        elif pilihan == 2:
            print(f"Hasil Pengurangan: {a - b}")
        elif pilihan == 3:
            print(f"Hasil Perkalian: {a * b}")
        elif pilihan == 4:
            if b != 0:
                print(f"Hasil Pembagian: {a / b}")
            else:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
        elif pilihan == 5:
            print(f"Hasil Pangkat: {a ** b}")
    else:
        print("Pilihan tidak valid!")

# Fungsi untuk perhitungan bangun datar
def bangun_datar():
    print("\n--- Perhitungan Bangun Datar ---")
    print("Pilih bangun datar yang ingin dihitung:")
    print("1. Persegi Panjang")
    print("2. Lingkaran")
    print("3. Segitiga")
    
    pilihan = int(input("Masukkan pilihan (1/2/3): "))
    
    if pilihan == 1:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        print(f"Luas Persegi Panjang: {luas}")
        print(f"Keliling Persegi Panjang: {keliling}")
    elif pilihan == 2:
        jari_jari = float(input("Masukkan jari-jari: "))
        luas = math.pi * jari_jari ** 2
        keliling = 2 * math.pi * jari_jari
        print(f"Luas Lingkaran: {luas}")
        print(f"Keliling Lingkaran: {keliling}")
    elif pilihan == 3:
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print(f"Luas Segitiga: {luas}")
    else:
        print("Pilihan tidak valid!")

# Fungsi untuk perhitungan bangun ruang
def bangun_ruang():
    print("\n--- Perhitungan Bangun Ruang ---")
    print("Pilih bangun ruang yang ingin dihitung:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    
    pilihan = int(input("Masukkan pilihan (1/2/3): "))
    
    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi kubus: "))
        volume = sisi ** 3
        luas_permukaan = 6 * sisi ** 2
        print(f"Volume Kubus: {volume}")
        print(f"Luas Permukaan Kubus: {luas_permukaan}")
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        volume = panjang * lebar * tinggi
        luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        print(f"Volume Balok: {volume}")
        print(f"Luas Permukaan Balok: {luas_permukaan}")
    elif pilihan == 3:
        jari_jari = float(input("Masukkan jari-jari tabung: "))
        tinggi = float(input("Masukkan tinggi tabung: "))
        volume = math.pi * jari_jari ** 2 * tinggi
        luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
        print(f"Volume Tabung: {volume}")
        print(f"Luas Permukaan Tabung: {luas_permukaan}")
    else:
        print("Pilihan tidak valid!")

# Menu utama
def main():
    while True:
        print("\n--- Menu Utama ---")
        print("1. Kalkulator Sederhana (Tambah, Kurang, Kali, Bagi, Pangkat)")
        print("2. Perhitungan Bangun Datar")
        print("3. Perhitungan Bangun Ruang")
        print("4. Keluar")
        
        pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
        
        if pilihan == 1:
            kalkulator()
        elif pilihan == 2:
            bangun_datar()
        elif pilihan == 3:
            bangun_ruang()
        elif pilihan == 4:
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    main()

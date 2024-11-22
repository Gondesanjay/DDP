#soal no 1
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit
print(celcius_ke_fahrenheit(0))    # Output: 32.0
print(celcius_ke_fahrenheit(100))  # Output: 212.0

#soal no 2
def is_genap(bilangan):
    return bilangan % 2 == 0
print(is_genap(4))  # Output: True
print(is_genap(7))  # Output: False

#soal no 3
def nilai(nilai):
    if nilai >= 70:
        print("lulus")        
    else:
        print("gagal") 
        
nilai(80)
nilai(60)

#soal no 4
def bilangan(a):
    hasil=[]

    for i in range(1, a):
        if i % 2 !=0:
            hasil.append(i)

    print(hasil)

bilangan(20)
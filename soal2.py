# Input angka
try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Inout tidak valid, mohon masukkan angka")
    sys.exit(1)

# Melakukan kalkulasi
hasil = 1
for i in range(1, angka + 1):
    hasil *= i

# Menampilkan hasil
print(f"Hasil dari nilai 1 sampai {angka} is: {hasil}")
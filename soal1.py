import datetime
import sys
from decimal import Decimal, ROUND_UP

# Deklarasi tahun ini
tahun_ini = datetime.datetime.now().year

# Mencek tahun kabisat
if tahun_ini % 4 == 0:
    if tahun_ini % 100 == 0:
        if tahun_ini % 400 == 0:
            total_tahun = 366
        else:
            total_tahun = 365
    else:
        total_tahun = 366
else:
    total_tahun = 365

# Input angka
try:
    number = int(input("Masukan angka: "))
except ValueError:
    print("Input tidak valid, masukkan angka.")
    sys.exit(1)

# Bagi angka dengan total hari dalam tahun ini
hasil = Decimal(number) / Decimal(total_tahun)

# Menampilkan hasil angka dengan total hari tahun ini
hasil = hasil.quantize(Decimal('0.00000000000'), rounding=ROUND_UP)
print("Hasil: ", hasil)
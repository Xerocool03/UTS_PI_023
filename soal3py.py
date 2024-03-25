import datetime

# Input
try:
    total_hari = int(input("Masukkan urutan hari: "))
except ValueError:
    print("Input tidak valid.")
    sys.exit(1)

# Ambil hari dan tanggal yang sekarang
now = datetime.datetime.now()

# Mengkalkulasikan hari kedepannya
tanggal = now + datetime.timedelta(days=total_hari)

# Print hasil
print(f"{tanggal.strftime('%A')} on {tanggal.strftime('%d %B %Y')}")
Nama = (input("Masukkan Nama : "))
Nim = int(input("Masukkan Nim : "))
UTS = int(input("Masukkan Nilai UTS : "))
UAS = int(input("Masukkan Nilai UAS : "))

# Menghitung nilai rata rata
rata_rata = (UTS + UAS) / 2

# Penyeleksian Kondisi
if rata_rata >= 81:
    Nilai = "A"
elif rata_rata >= 71:
    Nilai = "B"
elif rata_rata >= 61:
    Nilai = "C"
elif rata_rata >= 41:
    Nilai = "D"
else:
    Nilai = "E"

# Hasil ouput
print("Nama :", Nama)
print("NIM :", Nim)
print("Nilai Rata-Rata :", rata_rata)
print("Nilai yang anda dapatkan", Nilai)
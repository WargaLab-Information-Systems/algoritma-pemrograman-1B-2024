# input data
nama =input("Masukkan nama anda: ")
nim = input("Masukkan NIM anda: ")
nilaiUTS = int(input("Masukkan nilai UTS anda: "))
nilaiUAS = int(input("Masukkan nilai UAS anda: "))

# Mencari nilai rata-rata
nilaiRata = int((nilaiUTS + nilaiUAS) / 2)

# Hasil
print(f"Nama anda adalah {nama}")
print(f"NIM anda : {nim}")
print(f"Nilai rata rata anda : {nilaiRata}")

# Lanjutan hasil & menentukan nilai
if nilaiRata >= 81 <= 100:
    print("Anda mendapatkan nilai A")
elif nilaiRata >= 71 <= 80:
    print("Anda mendapatkan nilai B")
elif nilaiRata >= 61 <= 70:
    print("Anda mendapatkan nilai C")
elif nilaiRata >= 41 <= 60:
    print("Anda mendapatkan nilai D")
elif nilaiRata >= 0 <= 40:
    print("Anda mendapatkan nilai E") 
else:
    print("Angka anda Not Found")
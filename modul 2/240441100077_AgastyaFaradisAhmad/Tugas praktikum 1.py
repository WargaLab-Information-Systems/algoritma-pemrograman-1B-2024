nama = str(input("Masukkan nama anda: "))
nim = int(input("Masukkan nim anda: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

rata_rata = (uts + uas) / 2

if 100 >= rata_rata >= 81:
    nilai = "A"
elif 80 >= rata_rata >= 71:
    nilai = "B"
elif 70 >= rata_rata >= 61:
    nilai = "C"
elif 60 >= rata_rata >= 41:
    nilai = "D"
elif 40 >= rata_rata >= 0:
    nilai = "E"
else:
    nilai = "Nilai tidak valid"

print(f"Nama anda: {nama}")
print(f"Nim anda: {nim}")
print(f"Nilai rata-rata anda: {rata_rata:.2f}")
print(f"Anda mendapatkan nilai: {nilai}")

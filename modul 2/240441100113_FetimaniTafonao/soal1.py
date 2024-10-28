nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
uts = int(input("Masukkan Nilai UTS: "))
uas = int(input("Masukkan Nilai UAS: "))

rata_rata = (uts + uas) / 2

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

print("Nama Anda:", nama)
print("NIM Anda:", nim)
print("Nilai Rata-Rata Anda:", rata_rata)
print("Anda Mendapatkan Nilai:", Nilai)
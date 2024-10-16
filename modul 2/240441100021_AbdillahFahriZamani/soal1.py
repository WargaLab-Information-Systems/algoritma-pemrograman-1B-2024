# Input
nama = str(input("masukan nama :"))
nim = str(input("masukan nim :"))
nilai_uts = int(input("masukan nilai uts :"))
nilai_uas = int(input("masukan nilai uas :"))

# Rata-rata nilai
rata_rata = (nilai_uts + nilai_uas) / 2

# Penyeleksian Kondisi
if rata_rata >= 81 <= 100 :
    nilai = "Anda mendapat nilai A"

elif rata_rata >=71 <=80 :
    nilai = "Anda mendapat nilai B"

elif rata_rata >=61 <=70 :
    nilai = "Anda mendapat nilai C"

elif rata_rata >=41 <=60 :
    nilai = "Anda mendapat nilai D"

else :
    nilai = "Anda mendapat nilai E"

print(f"\nNama anda : {nama}")
print(f"NIM anda : {nim}")
print(f"Rata-rata nilai anda : {rata_rata}")
print(nilai)
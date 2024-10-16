Nama_Anda = input("masukkan nama anda:")
NIM = input("masukkan NIM:")
Nilai_UTS = int(input("masukkan nilai UTS:"))
Nilai_UAS = int(input("masukkan nilai UAS: "))
nilai_rata_rata = (Nilai_UTS + Nilai_UAS) / 2
print(f"Rata rata nilai anda:{nilai_rata_rata}")

if nilai_rata_rata >=81:
    print("Anda mendapatkan nilai A")
elif nilai_rata_rata >=71:
    print("Anda mendapatkan nilai B")
elif nilai_rata_rata >=61:
    print("Anda mendapatkan nilai C")
elif nilai_rata_rata >=41:
    print("Anda mendapatkan nilai D")
elif nilai_rata_rata <=40:
    print("Anda mendapatkan nilai E")
else:
    print("nilai tidak ada")

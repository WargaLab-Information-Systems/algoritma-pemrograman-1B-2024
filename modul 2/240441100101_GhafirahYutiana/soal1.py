nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
nilai_uts = float(input("Masukkan Nilai UTS: "))
nilai_uas = float(input("Masukkan Nilai UAS: "))

print(f"Mahasiswa atas nama = {nama}")
print(f"Dengan nim = {nim}")

rata_rata = (nilai_uts + nilai_uas) / 2
print(f"Nilai rata-rata anda: {rata_rata:}") 


if 81 <= rata_rata <= 100: 
    print("anda mendapatkan nilai A") 
elif 71 <= rata_rata <= 80:
    print("anda mendapatkan nilai B")
elif 61 <= rata_rata <= 70:
    print("anda mendapatkan nilai C")
elif 41 <= rata_rata <= 60:
    print("anda mendapatkan nilai D")
elif 0 <= rata_rata <= 40:
    print("anda mendapatkan nilai E")
else:
    print(" nilai yang didapatkan lebih dari 100 tidak ada kategori nilainya! silahkan input ulang")



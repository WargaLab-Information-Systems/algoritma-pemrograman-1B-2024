Nama = input("masukkan Nama =")
NIM =int(input("masukkan NIM ="))
Nilai_UTS =int(input("masukkan Nilai UTS ="))
Nilai_UAS =int(input("masukkan Nilai UAS ="))
print(f"Mahasiswa Atas Nama = {Nama} ")
print(f"Dengan NIM = {NIM} ")

rata_rata = (Nilai_UTS + Nilai_UAS) / 2
print("nilai rata-ratanya adalah: ",rata_rata,)

if rata_rata <= 40:
    print("anda mendapatkan nilai E")
elif rata_rata <= 60:
    print("anda mendapatkan nilai D")
elif rata_rata <= 70:
    print("anda mendapatkan nilai C")
elif rata_rata <= 80:
    print("anda mendapatkan nilai B")
elif rata_rata <=100:
    print("anda mendapatkan nilai A")
else:
    print("nilai yang anda masukkan lebih dari 100 coba input ulang")

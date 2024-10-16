# penyeleksian kondisi secara dinamis
nama = str(input("Masukkan Nama: "))
nim = int(input("Masukkan NIM: "))
nilai_uts = int(input("Masukkan Nilai UTS : "))
nilai_uas = int(input("Masukkan Nilai UAS : "))
nilai_ratarata = (nilai_uts + nilai_uas) / 2
print(f"Nilai rata-rata anda {nilai_ratarata}")

if nilai_ratarata > 80 <= 100:
    print("Anda mendapatkan nilai A")
elif nilai_ratarata > 70:
    print("Anda mendapatkan nilai B")
elif nilai_ratarata > 60:
    print("Anda mendapatkan nilai C")
elif nilai_ratarata > 40:
    print("Anda mendapatkan nilai D")
elif nilai_ratarata >= 0:
    print("Anda mendapatkan nilai E")
else:
    print("Nilai tidak valid")
    

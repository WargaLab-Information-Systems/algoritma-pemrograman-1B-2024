nama = str(input("Masukkan nama anda: "))
nim = int(input("Masukkan nim anda: "))
nilai_uts = int(input("Masukkan nilai uts anda: "))
nilai_uas = int(input("Masukkan nilai uas anda: "))

print(f"\nMahasiswa dengan nama: {nama} ")
print(f"Dengan nim: {nim}")

nilai_rata_rata = (nilai_uts + nilai_uas)/2
print("Nilai rata-rata anda adalah ", nilai_rata_rata)

if nilai_rata_rata >= 81 <= 100:
    print("Anda mendapatkan nilai A")
elif nilai_rata_rata >= 71 <= 80:
    print("Anda mendapatkan nilai B")
elif nilai_rata_rata >= 61 <= 70:
    print("Anda mendapatkan nilai C")
elif nilai_rata_rata >= 41 <= 60:
    print("Anda mendapatkan nilai D")
else:
    print("Anda mendapatkan nilai E")
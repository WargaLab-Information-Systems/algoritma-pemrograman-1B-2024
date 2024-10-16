name = str(input("Masukkan Nama: "))
nim = int(input("Masukkan NIM: "))
nilai_UTS = int(input("Masukkan nilai UTS: "))
nilai_UAS = int(input("Masukkan nilai UAS: "))
nilai = 0

nilaiRataRata = (nilai_UTS + nilai_UAS) / 2

if nilaiRataRata >= 81 <= 100:
    nilai = "A" 
elif nilaiRataRata >= 71 <= 80:
    nilai = "B"
elif nilaiRataRata >= 61 <= 70:
    nilai = "C" 
elif nilaiRataRata >= 41 <= 60:
    nilai = "D"
elif nilaiRataRata >= 0 <= 40:
    nilai = "E"
else:
    print("Type more correctly")


print(f"Nama anda adalah: {name}")
print(f"NIM anda: {nim}") 
print(f"Nilai UTS anda adalah: {nilai_UTS}")
print(f"Nilai UAS anda adalah: {nilai_UAS}")
print(f"Nilai rata rata anda adalah: {nilaiRataRata}")
print(f"Anda mendapat nilai {nilai}") 
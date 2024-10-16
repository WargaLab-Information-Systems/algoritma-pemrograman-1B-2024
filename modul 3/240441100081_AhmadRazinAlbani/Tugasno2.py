angka = int(input("Masukkan angka: "))
angka_balik = 0

while angka != 0:
    digit = angka % 10
    angka_balik = angka_balik * 10 + digit
    angka = angka // 10

print(f"Angka yang sudah dibalik: {angka_balik}")


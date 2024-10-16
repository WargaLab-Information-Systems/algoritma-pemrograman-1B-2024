angka = int(input("masukkan angka: "))
angka_secara_dinamis = str(angka)
angka_terbalik = ""

while angka_secara_dinamis:
    angka_terbalik += angka_secara_dinamis[-1]
    angka_secara_dinamis = angka_secara_dinamis[:-1]

print("Angka yang dibalik:", angka_terbalik)

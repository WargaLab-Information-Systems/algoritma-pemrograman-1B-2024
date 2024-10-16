angka = int(input("Masukkan angka: "))
angka_secara_dinamis = str(angka)
angka_terbalik = ""

for i in angka_secara_dinamis:
    angka_terbalik = i + angka_terbalik

print("Angka yang dibalik:", angka_terbalik)
angka = input("Masukkan angka bulat: ")

angka_balik = '' #sebagai string kosong
for digit in angka:
    angka_balik = digit + angka_balik

# hasil
print(f"Angka setelah dibalik: {angka_balik}")
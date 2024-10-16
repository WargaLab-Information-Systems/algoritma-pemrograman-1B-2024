angka = input("Masukkan angka bulat: ")
hasil = ""

for digit in angka:
    hasil = digit + hasil

print(f"Angka setelah dibalik: {hasil}")
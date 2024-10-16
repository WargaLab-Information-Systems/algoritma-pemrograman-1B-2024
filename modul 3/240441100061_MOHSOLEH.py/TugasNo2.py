# Membalikkan urutan angka secara Dinamis

angka = input("Masukkan angka bulat yang di inginkan sudarso : ")

if angka.isdigit():
    # Membalik urutan angka dengan slicing
    angka_terbalik = angka[::-1]
    print("Angka setelah dibalik:", angka_terbalik)
else:
    print("Input harus berupa angka!")

# test
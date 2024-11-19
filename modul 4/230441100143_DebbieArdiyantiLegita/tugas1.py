karakter = input("Masukkan Karakter [X atau O]: ").upper()
if karakter not in ("X", "O"):
    print("Karakter tidak valid! Harap masukkan X atau O.")

sisi = int(input("Masukkan Panjang Sisi: "))
if sisi <= 0:
    print("Panjang Sisi tidak valid! Harap masukkan angka positif.")

invers = "O" if karakter == "X" else "X"

for i in range(-sisi + 1, sisi):
    baris = ""
    panjang = 2 * (sisi - abs(i)) - 1

    for j in range(panjang):
        if j % 2 == 0:
            baris += karakter
        else:
            baris += invers

    print(baris.center(2 * sisi - 1))
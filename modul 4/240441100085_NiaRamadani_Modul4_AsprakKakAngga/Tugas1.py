while True :
    Karakter = input("Masukkan karakter X atau O :")
    if Karakter == 'X' or Karakter =='O' :
        break
    else:
        print("Input tidak valid, harap masukkan karakter 'X' atau 'O' ")

Ukuran_sisi = int(input("Masukkan ukuran sisi belah ketupat :"))

for i in range (Ukuran_sisi):
    spasi = Ukuran_sisi - i - 1
    print(" " * spasi, end= "")
    for j in range(i + 1) :
        if (j + spasi) % 2 == 0:
            print(Karakter, end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(Ukuran_sisi - 1):
    spasi = i + 1
    print(" " * spasi, end="")
    for j in range(Ukuran_sisi - spasi):
        if (j + spasi) % 2 == 0:
            print(Karakter, end=" ")
        else:
            print(" ", end=" ")
    print()

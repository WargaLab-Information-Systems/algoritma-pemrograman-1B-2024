n = int(input("Masukkan Ukuran : "))
karakter = input("Masukkan karakter antara (X / O) : ").upper()

if karakter == "X" or karakter == "O": # or jika nilai salah satunya benar maka benar
    for i in range(n): # sesuai dengan ukuran yg di masukkan (n)
        for j in range(n - i - 1): # menentukan jumlah spasi yang dicetak misalnya 7 - 0 - 1=6 di pinggir
            print(" ", end="") # digunakan untuk mencetak karakter dan spasi tanpa berpindah ke baris baru end
        for j in range(i + 1): # mencetak huruf yang dimasukkan jadi tambah 1 dan seterusnya
            print(karakter + " ", end="")
        print() #mencetak baris baru

    for i in range(n - 1):
        for j in range(i + 1): # mencetak spasi di pinggir
            print(" ", end="")
        for j in range(n - i - 1):
            print(karakter + " ", end="")
        print()
else:
    print("Karakter tidak valid. Silakan masukkan 'X' atau 'O'.")

# elif karakter == "O":
#     for i in range(n):
#         for j in range(n - i - 1):
#             print(" ", end="")
#         for j in range(i + 1):
#             print(karakter + " ", end="")
#         print()

#     for i in range(n - 1):
#         for j in range(i + 1):
#             print(" ", end="")
#         for j in range(n - i - 1):
#             print(karakter + " ", end="")
#         print()
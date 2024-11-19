N = int(input("Masukkan panjang sisi belah ketupat: "))
while True:
    karakter = input("Masukkan karakter untuk pola (X/O): ")
    if karakter == 'X' or karakter == 'O':
        break
    else:
        print("Input tidak valid, karakter harus X / O!!!")

# cetak setengah atas (termasuk tengah)
for i in range(N):
    print(" " * (N - i - 1), end="") # cetak spasi untuk merapikan ke tengah
    print(karakter * (2 * i + 1)) # cetak pola dengan karakter

# cetak setengah bawah belah ketupat
for i in range(N - 2, -1, -1):
    # cetak spasi untuk merapikan ke tengah
    print(" " * (N - i - 1), end="") # tdk mnmbahkan baris barus stelah spasi
    print(karakter * (2 * i + 1))

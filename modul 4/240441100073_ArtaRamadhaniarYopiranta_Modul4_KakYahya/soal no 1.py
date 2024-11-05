a = int(input("Masukkan ukuran sisi belah ketupat: "))
karakter = input("Masukkan karakter pilihan (misalnya X/O): ")

total_baris = 2 * a - 1


for i in range(total_baris):
    if i < a:
        spasi = a - i- 1
    else:
        spasi = i- a + 1

    baris = ""
    for j in range(total_baris):
        if (j >= spasi and j < total_baris - spasi) and ((i + j) % 2 == 0): 
            print(karakter, end="")
        else:
            print(" ", end="")
    print()
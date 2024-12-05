k = (input("Masukkan karakter pilihan anda (X / O): "))
n = int(input("Masukkan ukuran sisi N : "))
if k == "X" or k == "O":
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print(k + " ", end="")
        print()
    for i in range(n - 1):
        for j in range(i + 1):
            print(" ", end="")
        for j in range(n - i - 1):
            print(k + " ", end="")
        print()
        
else:
    print("Silakan coba lagi, masukkan (X / O)")
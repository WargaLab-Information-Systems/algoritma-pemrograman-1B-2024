karakter = input("Masukkan karakter (x/o): ")
n = int(input("Masukkan ukuran sisi N: "))

if karakter not in ['x', 'o']:
    print("Karakter harus 'x' atau 'o'.")
else:
    for i in range(n * 2 - 1):
        for j in range(n * 2 - 1):
            if abs(n - 1 - i) + abs(n - 1 - j) < n:  #rumus manhattan distance
                print(karakter if (i + j) % 2 == 0 else ' ', end='')
            else:
                print(' ', end='')
        print()  

karakter = input("Masukkan karakter (misalnya 'X' atau 'O'): ").lower()
N = int(input("Masukkan ukuran sisi (N): "))

for i in range(N):
    print(' ' * (N - i - 1))
    for j in range(2 * i + 1):
        print(karakter if j % 2 == 0 else ' ', end='')
    print()

for i in range(N - 2, -1, -1):
    print(' ' * (N - i - 1))
    for j in range(2 * i + 1):
        print(karakter if j % 2 == 0 else ' ', end='')
    print()

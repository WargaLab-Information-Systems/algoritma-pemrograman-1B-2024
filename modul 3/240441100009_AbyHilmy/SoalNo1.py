size = int(input("Masukkan size angka : "))

# mambuat pola angka dengan menggunakan x pola angka 0
for kolom in range(size):
    for baris  in range(size):
        if   kolom  == 0 or kolom == size - 1  or baris  == 0 or baris == size - 1 :
            print("X", end="")
        else:
            print(" ", end="")
    print()
print("")

# mambuat pola angka dengan menggunakan x pola angka 0
for kolom in range(size):
    for baris  in range(size):
        if   kolom  == 0 or kolom  == size - 1  or baris  == 0 or baris == size - 1 :
            print("X", end="")
        else:
            print(" ", end="")
    print()
print("")

#membuat pola angka dengan menggunakan x pola angka 9
for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print('X' * size)
    elif i < size // 2:
        print('X' + ' ' * (size - 2) + 'X')
    else:
        print(' ' * (size - 1) + 'X')
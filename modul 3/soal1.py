size = int(input("Masukkan size: "))

for baris in range(size):
    for kolom in range(size):
        if baris == 0 or baris == size - 1 or kolom == 0 or kolom == size - 1:
            print("0", end="")
        else:
            print(" ", end="")
    print()

print()

for baris in range(size):
    for kolom in range(size):
        if baris == 0 or baris == size - 1 or kolom == 0 or kolom == size - 1:
            print("0", end="")
        else: 
            print(" ", end="")
    print()

print()

for baris in range(size):
    for kolom in range(size):
        if baris == 0 or baris == size // 2 or baris == size - 1:
            print("5", end="")
        elif baris < size // 2 and kolom == 0:
            print("5", end="")
        elif baris > size // 2 and kolom == size - 1:
            print("5", end="")
        else:
            print(" ", end="")
    print()
    
print()



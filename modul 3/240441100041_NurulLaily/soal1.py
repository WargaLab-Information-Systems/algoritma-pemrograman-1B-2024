size = int(input("Masukkan size: "))

# Angka 0
for i in range(size):
    if i == 0 or i == size - 1:
        print("x" * size)
    else:
        print("x" + (" " * (size - 2)) + "x")
print()

# Angka 4
for i in range(size):
    for j in range(size):
        if (j == 0 and i <=size-4) or (j == size - 1) or (i==size // 2):
            print("x", end="")
        else:
            print(" ", end="")
    print()
    
# Angka 1
for i in range(size):
    print("   x   ")
print()
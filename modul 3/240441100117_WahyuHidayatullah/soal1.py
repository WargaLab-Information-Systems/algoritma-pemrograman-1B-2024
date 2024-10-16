size = int(input("Masukkan size: "))

# angka 1
for i in range(size):
    print("" * (size) + "x")
print()

# angka 1
for i in range(size):
    print("" * (size)+"x")
print()

# angka 7
for i in range(size):
    if i == 0:
        print("x" * size)
    else:
        print(" " * (size - 1) + "x")
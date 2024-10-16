# Masukkan ukuran yang anda mau
size = int(input("Masukkan Size : "))

# angka 0
for i in range(size):
    if i == 0 or i == size - 1:
        print("x" * size)
    else:
        print("x" + " " * (size - 2) + "x")

print()

# angka 6
for i in range(size):
    if i == 0 or i == size - 1 or i == size // 2:
        print("x" * size)
    elif i < size // 2:
        print("x")
    else:
        print("x" + " " * (size - 2) + "x")

print()

# angka 1
for i in range(size):
    if i == 0:
        print("x"*1)
    else:
        if i == 1:
            print("" + "x")
        else:
            print("" + "x")

# test
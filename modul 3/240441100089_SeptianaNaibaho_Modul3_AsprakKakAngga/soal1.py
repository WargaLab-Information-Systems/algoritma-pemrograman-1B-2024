size = int(input("Masukan Size : "))

if size < 3:
    print("Size harus lebih dari 3.")
else:
    for row in range(size):
        if row == 0 or row == size-1:
            print("x" * size)
        else:
            print("x" + " " * (size-2) + "x")
    print()

    for row in range(size):
        if row == 0 or row == size-1 or row == size//2:
            print("x" * size)
        else:
            print("x" + " " * (size-2) + "x")
    print()

    for row in range(size):
        if row == 0 or row == size-1 or row == size//2:
            print("x" * size)
        elif row < size // 2:
            print("x" + " " * (size-2) + "x")
        else:
            print(" " * (size-1) + "x")
    print()








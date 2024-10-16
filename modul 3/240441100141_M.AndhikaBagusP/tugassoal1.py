size = int(input("Masukkan size: "))

for row in range(size):
    for col in range(size):
        if col==size//2:
            print("X", end = " ")
        else:
            print(" ",  end = " ")
    print()
print()

for row in range(size*2):
    for col in range(size):
        if (col==0 and row<=size-1) or (col==size-1 and row<=size+3) or (row==size-1):
            print("X", end = " ")
        else:
            print(" ", end = " ")
    print()

for row in range(size):
    for col in range(size):
        if col==size//2:
            print("X", end = " ")
        else:
            print(" ",  end = " ")
    print()
print()
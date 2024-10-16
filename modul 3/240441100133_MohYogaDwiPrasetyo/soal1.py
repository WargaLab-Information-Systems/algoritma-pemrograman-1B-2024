size = int(input("Masukkan size: "))

# nim = 133

# angka 1
for i in range(size):
    print("X")
print()

# angka 3
for i in range(size):
    if i == 0 or i == size//2 or i == size-1:
        print("X" * size)
    else:                      
        pass # placeholder
        print(" " * (size-1) + "X")
print()
        
# angka 3
for i in range(size):
    if i == 0 or i == size//2 or i == size-1:
        print("X" * size)
    else:
        pass
        print(" " * (size-1) + "X")
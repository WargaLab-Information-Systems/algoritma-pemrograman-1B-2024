size= int(input("Masukkan ukuran : "))

# membentuk angka 0
for i in range (size):
    if i == 0:
        print("#"*size)
    elif i == size - 1:
        print("#"*size)
    else :
        print("#" + " " * (size-2) + "#")
      
print()

# membentuk angka 5
for i in range (size):
    if i == 0:
        print("#" * size)
    elif i < (size//2):
        print("#")
    elif i == size // 2:
        print("#"*size)
    elif i == (size - 1):
        print("#"*size)
    else:
        print(" " * (size - 1) + "#")

print()

# membentuk angka 3
for i in range (size):
    if i == 0:
        print("#" * size)
    elif i == size-1 or i == (size // 2) :
        print("#"* size)
    elif i <(size // 2):
        print(" " * (size-1) + "#")
    else:
        print(" " * (size-1) + "#")
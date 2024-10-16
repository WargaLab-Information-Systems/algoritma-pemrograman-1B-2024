size = int(input("Masukan size: "))

#Angka 0
for i in range(size):
    if i == 0 or i == size - 1:
        print("x" * size)
    else:
        print("x" + (" " * (size - 2)) + "x") 
print()

# Angka 7
print("x" * size) 
for i in range(1, size):  
    print(" " * (size - 1) + "x")
print()

# Angka 3
for i in range(size):
    if i == 0 or i == size - 1 or i == size // 2: 
        print("x" * size)
    else:
        print(" " * (size - 1) + "x") 
print()
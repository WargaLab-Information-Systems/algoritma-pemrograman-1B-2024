# Menginputkan size
size = int(input("masukan size :"))

# Angka 0
for i in range(size):
    if i == 0 or i == size - 1 :
        print("x" * size)                       # Baris atas dan bawah
    else:
        print("x" + (" " * (size - 2)) + "x")   # Baris kiri dan kanan
print()

# Angka 2
print("x" * size)                   # Baris paling atas
for i in range(size // 2 - 1):
    print(" " * (size - 1) + "x")   # Kolom ke 2 dan 3
print("x" * size)                   # Baris tengah
for i in range(size // 2 - 1):
    print("x" + " " * (size - 1))  # Kolom ke 5 dan 6
print("x" * size)                   # Baris paling bawahd
print()

# Angka 1
for i in range(size):
    if i == 0:
        print("x" * (size - 3))         # Baris atas
    elif i < size - 1:
        print(" " * (size - 4) + "x")   # Batang
    else:
        print("x" * size)               # Baris dasar
print()

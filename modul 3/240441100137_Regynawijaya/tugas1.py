# angka 1
size = int(input('masukan size : '))

for i in range(size):
    print("  x  ")

print()

# angka 3
for i in range(size) :
    if i == 0 or i == size // 2 or i == size - 1:
<<<<<<< HEAD
        print("x" * size)  
=======
        print("x" * size)  #baris paling atas, tengah, bawah
>>>>>>> b3e79c8a53c62208c17d1c4a655789f4143997d0
    else:
        print(" " * (size - 1)+ "x") #garis kanan
print() #baris kosong untuk spasi antar angka

# angka 7
for i in range(size):
    if i == 0:
        print("x" * size)
    else:
        print(" " * (size - 1) + "x")


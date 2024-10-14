# angka 1
size = int(input('masukan size : '))

for i in range(size):
    print("  x  ")

print()

# angka 3
for i in range(size) :
    if i == 0 or i == size // 2 or i == size - 1:
        print("x" * size)  #baris paling atas, tengah, bawah
    else:
        print(" " * (size - 1)+ "x") #garis kanan
print() #baris kosong untuk spasi antar angka

# angka 7
for i in range(size):
    if i == 0:
        print("x" * size)
    else:
        print(" " * (size - 1) + "x")


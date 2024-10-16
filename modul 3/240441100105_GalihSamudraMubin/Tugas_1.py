size = int(input("Masukkan tinggi Bentuk: "))
spasi = int(size/2)

for i in range (size):
    print(" " * (size // 2) + "x")
print()  

print("x" * size)
for i in range(size-2):
    print("x" + " " * (size - 2) + "x")
print("x" * size)
print()  

print("x" * size)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
for i in range(1, spasi):
    print("x")
print("x" * size)
for i in range(1, spasi):
    print(" " * (size - 1) + "x")
print("x" * size)

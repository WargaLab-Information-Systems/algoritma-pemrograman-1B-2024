#Menginput size
size = int(input("masukkan size:"))

#pola untuk angka 0
for i in range(size): #menjalankan kode sesuai size
    if i == 0 or i == size - 1:
        print("x" * size) #baris atas dan bawah
    else:
        print("x" + " " * (size - 2)+ "x")  #baris kiri dan kanan
print()

#pola untuk angka 3
for i in range (size):
    if i == 0 or i == size // 2 or i == size - 1:
        print("x" * size) #Baris paling atas, tengah, dan bawah
    else:
        print(" " * (size - 1) + "x")
print()

#3
for i in range (size):
    if i == 0 or i == size // 2 or i == size - 1:
        print("x" * size) #Baris paling atat, tengah, dan bawah
    else:
        print(" " * (size - 1) + "x") #Garis kanan


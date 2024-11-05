size = int(input("masukkan ukuran : "))
bentuk = str(input("masukkan bentuk (X/O) : "))
while bentuk != "X" and bentuk != "O":
    bentuk = str(input("masukkan bentuk (X/O) : "))
for i in range(1, size + 1):
    for j in range (size - i):
        print(" ", end="")
    for k in range (1, i + 1):
        print(bentuk + " ", end="")
    print()
for i in range(1, size + 1): 
    for k in range (1, i + 1):
        print(" ", end="")
    for j in range (size - i):
        print(bentuk + " ", end="")
    print()

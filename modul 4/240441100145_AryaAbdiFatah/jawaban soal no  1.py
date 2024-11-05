size = int(input("masukan ukuran:"))
motif = str(input("masukan motif (X/O) : "))

while motif !="X" and motif !="O":
    motif = str(input("masukan motif (X/O) : "))
for i in range (1, size + 1):
    for j in range (size - i):
        print("*", end="")
    for k in range (1, i + 1):
        print(motif + " ", end="")
    print()
for i in range(1, size + 1):
    for k in range (1, i + 1):
        print("*", end="")
    for j in range (size - i):
        print(motif + " ",end="")
    print()
angka = int(input("Masukkan angka: "))
bin = ""
while angka > 0:
    bin = str(angka % 2) + bin
    angka //= 2
for i in range(len(bin)):
    print(bin[:i+1])
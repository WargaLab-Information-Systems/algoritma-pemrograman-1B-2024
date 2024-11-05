# Mengonversi bilangan desimal ke bilangan biner
# dalam bentuk pola segitiga


angka = int(input("Masukkan bilangan desimal (basis 10) : "))

# Mengonversikan angka

biner = " "
while angka > 0 :
    a = angka % 2
    biner = str(a) + biner
    angka //= 2
print("Bilangan biner dari bilangan desimal tersebut adalah ", biner)

print("Pola bilangan dari bilangan biner tersebut adalah : ")
for i in range (len(biner)):
    for j in range (i):
        print(biner[j], end=" ")
    print()

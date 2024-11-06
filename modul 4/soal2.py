# Input
desimal = int(input("Masukkan bilangan desimal: "))

# Mengonversi bilangan
biner = "" #100
# n = angka_desimal

if desimal == 0:
    biner = "0"
else:
    while desimal > 0:
        biner = str(desimal % 2) + biner
        desimal //= 2

# Menampilkan bilangan biner
print("Bilangan biner:", biner)

# Mencetak pola
print("Pola segitiga:")
for i in range(1, len(biner) + 1):
    print(biner)

print(len(biner))
# Input dari pengguna
angka_desimal = int(input("Masukkan bilangan desimal: "))

# Mengonversi desimal ke biner
if angka_desimal == 0:
    angka_biner = "0"
else:
    angka_biner = ""
    n = angka_desimal
    while n > 0:
        angka_biner = str(n % 2) + angka_biner
        n //= 2

# Mencetak pola segitiga
for i in range(1, len(angka_biner) + 1):
    print(angka_biner[:i])
print(len(angka_biner))
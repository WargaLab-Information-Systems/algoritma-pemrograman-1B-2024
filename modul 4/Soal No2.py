# Mengambil input dari pengguna
desimal = int(input("Masukkan bilangan desimal: "))

# Konversi desimal ke biner secara manual
biner = ''
if desimal == 0:
    biner = '0'
else:
    while desimal > 0:
        biner = str(desimal % 2) + biner
        desimal //= 2

# Menampilkan pola segitiga
i = 1
while True:
    if i <= 0:
        break

    angka = biner[i - 1:i]
    if angka == '':
        break

    print(biner[:i])
    i += 1



# # Menampilkan pola segitiga
# for i in range(1, (biner) + 1):
#     print(biner[:i])
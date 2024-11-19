desimal = int(input("Masukkan bilangan desimal: "))

biner = ""
angka = desimal

# Konversi desimal ke biner
while angka > 0:
    biner = str(angka % 2) + biner  # Tambahkan sisa bagi 2 ke awal string
    angka //= 2  # Bagi angka dengan 2

print(f"Bilangan biner dari {desimal} adalah: {biner}")
 
panjang = 0
for _ in biner:
    panjang += 1

print("Pola Segitiga:")
for i in range(1, panjang + 1):
    for j in range(i):
        print(biner[j], end=" ")
     
    print()

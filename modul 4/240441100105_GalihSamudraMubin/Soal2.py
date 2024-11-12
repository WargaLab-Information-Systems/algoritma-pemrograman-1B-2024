bil_desimal = int(input("Masukkan bilangan desimal: "))

bil_biner = ""
while bil_desimal > 0:
    bil_biner = str(bil_desimal % 2) + bil_biner
    bil_desimal //= 2
bil_biner = bil_biner or "0"

# Menampilkan hasil dan pola segitiga
print("Hasil konversi biner:", bil_biner)
print("\nPola segitiga:")
for i in range(1, len(bil_biner) + 1):
    print(bil_biner[:i])
angka_desimal = int(input("Masukan angka desimal (bilangan bulat): "))
panjang_biner = 0 
biner = " "
angka = angka_desimal

while angka > 0:
    biner = str(angka % 2) + biner 
    angka = angka // 2 
    panjang_biner += 1

print(f"hasil konversi ke biner:", {biner})
print("pola segitiga")
for i in range (1, panjang_biner + 1):
    print(biner[:i])
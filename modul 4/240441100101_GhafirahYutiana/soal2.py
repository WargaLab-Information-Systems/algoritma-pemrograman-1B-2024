angka_desimal = int(input("masukkan angka desimal:"))

biner = ""
angka = angka_desimal
while angka >0:
    biner = str(angka % 2) + biner
    angka = angka // 2

print(f"hasil konversi ke biner:", {biner})
print("pola segitiga")
for i in range (1,len(biner)+ 1):
    print(biner[:i])
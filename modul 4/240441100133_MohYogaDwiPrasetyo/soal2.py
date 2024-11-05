while True:
    desimal = int(input("Masukkan bilangan desimal: "))
    if desimal < 0:
        print("Masukkan bilangan desimal positif!")
        continue
    break
    
# konversi desimal ke biner
desimal_awal = desimal # simpan nilai awal desimal
biner = "" # inisialisasi variabel simpan string
if desimal == 0: 
    biner = "0" 
else:
    while desimal > 0:
        biner = str(desimal % 2) + biner
        desimal = desimal // 2

print("\nHasil Konversi:")
print(f"Desimal: {desimal_awal}")
print(f"Biner  : {biner}")

# pola segitiga
print("\nPola Segitiga Biner:")
for i in range(1, len(biner) + 1):
    # buat spasi di awal setiap baris untuk membentuk segitiga
    for j in range(len(biner) - i):
        print(" ", end="")
    
    # cetak i digit pertama dari bilangan biner
    for j in range(i):
        print(biner[j], end="")
    print() 


# Input bilangan desimal
desimal = int(input("Masukkan bilangan desimal: "))
n = desimal
biner = ""

# Mengonversi bilangan desimal ke biner menggunakan loop
while n > 0:
    biner = str(n % 2) + biner
    n = n // 2

print(f"Hasil konversi ke biner: {biner}")

# Menampilkan pola segitiga menggunakan nested loops
print("\nPola segitiga:")
panjang = len(biner)
for i in range(1, panjang + 1): 
    for j in range(i):  
        print(biner[j], end="")  # untuk membuat pola segitiga dari representasi biner secara bertahap.
    print()  
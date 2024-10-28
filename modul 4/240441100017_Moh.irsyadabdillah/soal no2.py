# input bilangan desimal
bilangan_desimal = int(input("Masukkan bilangan desimal: "))

bilangan_biner = ''  # Variabel untuk menyimpan hasil konversi biner
n = bilangan_desimal  # Salin bilangan desimal ke variabel sementara

# konversi desimal ke biner
while n > 0:
    sisa = n % 2  # Ambil sisa pembagian (0 atau 1)
    bilangan_biner = str(sisa) + bilangan_biner  # Tambahkan sisa ke hasil biner
    n = n // 2  

# Langkah 2: Mencetak pola segitiga dari hasil biner
panjang_biner = len(bilangan_biner)  # Panjang dari bilangan biner

for i in range(1, panjang_biner +1):
    print(bilangan_biner[:i])  
# sisa = 0,5 % 2 = #0,1
# print(sisa)

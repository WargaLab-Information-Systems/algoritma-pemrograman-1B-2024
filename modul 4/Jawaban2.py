# input dari pengguna 
angka_desimal = int(input("Masukkan bilangan desimal: "))

# variabel untuk menyimpan desimal ke biner
angka_biner = ""  # Menyimpan hasil biner sebagai string
sisa_bagi = angka_desimal  # Menyimpan nilai desimal yang akan dirubah

while sisa_bagi > 0: # akan berhenti jika sisa bagi menjadi 0
    angka_biner = str(sisa_bagi % 2) + angka_biner  
    sisa_bagi = sisa_bagi // 2  

print("Bilangan biner:")
print(angka_biner)

# pola segitiga dari bilangan biner
print("Pola Segitiga:")

for i in range(1, len(angka_biner) + 1): #mengukur panjang string biner 
    for j in range(i):
        print(angka_biner[j], end="")  # Cetak karakter satu per satu j Digunakan untuk mengakses karakter dari string angka_biner
    print("")  # Ganti baris setelah setiap iterasi

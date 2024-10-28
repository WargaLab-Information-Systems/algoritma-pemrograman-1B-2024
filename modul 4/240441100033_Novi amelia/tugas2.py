angka_desimal = int(input("masukkan angka desimal: "))
panjang_biner = 0

biner  = "" #menyimpan hasil konversi biner
angka = angka_desimal
while angka >0: # akan terus berjalan selama nilai angka lebih besar dari nol
    biner = str(angka % 2) + biner #cara dasar untuk mengkonversi
    angka = angka // 2
    panjang_biner += 1
    
print(f"hasil konversi ke biner:", {biner})
print("pola segitiga")
for i in range (1,panjang_biner + 1):
    print(biner[:i]) #mencetak subtring #mengambil 1 karakter setiap baris


















# # Meminta input bilangan desimal dari pengguna
# bilangan_desimal = int(input("Masukkan bilangan desimal: "))

# # Konversi desimal ke biner tanpa fungsi bawaan bin()
# biner = ""
# angka = bilangan_desimal
# while angka > 0:
#     sisa = angka % 2
#     biner = str(sisa) + biner
#     angka = angka // 2

# # Menampilkan hasil konversi biner
# print("Hasil konversi ke biner:", biner)
# print("pola segitiga")

# # Menampilkan pola segitiga sama sisi
# panjang = len(biner)
# for i in range(1, panjang + 1):
#     spasi = ' ' * (panjang - i)  # Menambahkan spasi di kiri untuk membentuk segitiga
#     print(spasi + ' '.join(biner[:i]))  # Menambahkan spasi antar-digit agar rapi
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
    

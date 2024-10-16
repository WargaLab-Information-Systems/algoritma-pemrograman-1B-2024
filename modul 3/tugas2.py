angka_input = int(input("Masukkan angka bulat: "))
angka_dibalik = 0

while angka_input > 0:
    sisa = angka_input % 10
    angka_input = angka_input//10
    angka_dibalik = (angka_dibalik*10) + sisa
    
print(f"Urutan angka bulat yang dibalik menjadi {angka_dibalik}")
 
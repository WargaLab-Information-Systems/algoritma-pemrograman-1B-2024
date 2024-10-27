angka = int(input("Masukkan angka bulat: "))

# variabel untuk menyimpan hasil angka terbalik
angka_terbalik = "" #menyimpan hasil akhir setelah angka dibalik

# Loop angka negatif
if angka[0] == '-':
    for digit in angka[:0:-1]:  # Membalik angka dari belakang tanpa tanda negatif
        angka_terbalik += digit
    angka_terbalik = '-' + angka_terbalik # digit yang terbalik bakal ditambahin ke variabel angka terbalik 
else:
    # Loop angka positif
    for digit in angka[::-1]:  # ngambil angka dari belakang ke depan
        angka_terbalik += digit

print("Angka setelah dibalik:", angka_terbalik)
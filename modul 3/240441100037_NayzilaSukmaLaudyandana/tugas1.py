#membuat angka 0
tinggi = int(input("Masukkan tinggi angka : "))

print("")
# Membentuk angka 0
for i in range(tinggi):
    # Baris pertama dan terakhir
    if i == 0 or i == tinggi - 1:
        print('x' * tinggi)
    # Baris tengah
    else:
        print('x' + ' ' * (tinggi - 2) + 'x')
print()  # Memisahkan pola 0 dan 1 dengan baris kosong


#membuat angka 3
for i in range(tinggi):
    # Baris pertama, tengah, dan terakhir
    if i == 0 or i == tinggi - 1 or i == tinggi // 2:
        print('x' * tinggi)
    # Baris sebelum tengah
    elif i < tinggi // 2:
        print(' ' * (tinggi - 1) + 'x')
    # Baris setelah tengah
    else:
        print(' ' * (tinggi - 1) + 'x')


# Menggambar angka 7
for i in range(tinggi): # Baris pertama
    if i == 0:  
        print('x' * tinggi)  
    elif i < tinggi - 1:  # Baris di atas terakhir
        print(' ' * (tinggi - 1 - i) + 'x') 
    else:  # Baris terakhir
        print('x')  

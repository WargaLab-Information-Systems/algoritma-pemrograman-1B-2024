# Meminta input ukuran
size = int(input("Masukkan Size: "))

# Pola angka 0
for i in range(size):
    if i == 0 or i == size - 1:
        print('x' * size)  # Baris atas dan bawah
    else:
        print('x' + ' ' * (size - 2) + 'x')  # Baris tengah

print()

# Pola angka 6
for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print('x' * size)  # Baris atas, tengah, dan bawah
    elif i < size // 2:
        print('x')  # Bagian kiri saja (atas)
    else:
        print('x' + ' ' * (size - 2) + 'x')  # Bagian kiri dan kanan (bawah)

print()

# Pola angka 9
for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print('x' * size)  # Baris atas, tengah, dan bawah
    elif i < size // 2:
        print('x' + ' ' * (size - 2) + 'x')  # Bagian kiri dan kanan (atas)
    else:
        print(' ' * (size - 1) + 'x')  # Bagian kanan saja (bawah)





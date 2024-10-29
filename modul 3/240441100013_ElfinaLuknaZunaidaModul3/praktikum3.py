
size = int(input("Masukan Size : "))

# Membentuk angka 0
for i in range(size):
    if i == 0 or i == size - 1:
        print('x' * size)
    else:
        print('x' + ' ' * (size - 2) + 'x')
 
print()

# Membentuk angka 1
for i in range(size):
    print(' ' * (size // 2) + 'x') 

print()  

# Membentuk angka 3
for i in range(size):
    # Baris pertama, tengah, dan terakhir
    if i == 0 or i == size - 1 or i == size // 2:
        print('x' * size)
    # Baris sebelum tengah
    elif i < size // 2:
        print(' ' * (size - 1) + 'x')
    # Baris setelah tengah
    else:
        print(' ' * (size - 1) + 'x')



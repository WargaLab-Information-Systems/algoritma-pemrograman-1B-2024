n = int(input("Masukkan ukuran N: "))
while True:
   pola = input("Masukkan pola (X/O): ")
   if pola == 'X' or pola == 'O':
       break
   else:
       print("Pola harus X/O: ")
# Bagian atas ketupat
for i in range(n):
    for j in range(n-i):
        print(' ', end='')
    for k in range(i+1):
        print(pola, end=' ')
    print()
# Bagian bawah ketupat
for i in range(n-1):
    for j in range(i+2):
        print(' ', end='')
    for k in range(n - i -1):
        print(pola, end=' ')
    print()
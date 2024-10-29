lebar_belah_ketupat = int(input('Input lebar belah ketupat: '))
karakter = input("Masukkan karakter untuk pola checkerboard (misalnya 'X' atau 'O'): ")
print()

for i in range(lebar_belah_ketupat):
  for j in range(lebar_belah_ketupat-i):
    print(' ',end='')
      
  for k in range(i+1):
    print(f'{karakter} ',end='')
  print()
 
for i in range(1,lebar_belah_ketupat):
  for j in range(i+1):
    print(' ',end='')
      
  for k in range(lebar_belah_ketupat-i):
    print(f'{karakter} ',end='')
  print()
lebar_belah_ketupat = int(input("masukkan lebar belah ketupat: "))
karakter = input("Masukkan karakter untuk pola checkerboard (misalnya 'X' atau 'O'): ")
print()
  
for i in range(lebar_belah_ketupat):
  for j in range(lebar_belah_ketupat-i):
    print(' ',end='') #0ke6 dan seterusnya
      
  for k in range(i+1):
    print(f'{karakter} ',end='') #0ke0 dan seterusnya
  print()
 
for i in range(1,lebar_belah_ketupat):
  for j in range(i+1): #0ke1 dan seterusnya
    print(' ',end='')
      
  for k in range(lebar_belah_ketupat-i):
    print(f'{karakter} ',end='') #0ke5 dan seterusnya
  print()
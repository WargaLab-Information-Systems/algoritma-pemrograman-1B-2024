
lebarKetupat = int(input("masukkan lebar ketupat"))
karakter = str(input("pilih karakter yang ingin di cetak"))
for i in range(lebarKetupat):
  for j in range(lebarKetupat-i):
    print(" ",end="")
      
  for k in range(i+1):
    print(f"{karakter} ",end="")
  print()
 
for i in range(1,lebarKetupat):
  for j in range(i+1):
    print(" ",end="")
      
  for k in range(lebarKetupat-i):
    print(f"{karakter} ",end="")
  print()

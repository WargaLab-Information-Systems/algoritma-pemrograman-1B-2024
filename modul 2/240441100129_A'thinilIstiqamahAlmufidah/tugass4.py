tahun = int(input("masukkan tahun : "))

if (tahun % 4 == 0)and (tahun % 100 != 0):
    print (tahun,"adalah tahun kabisat")
elif (tahun % 400 == 0):
    print(tahun,"adalah tahun kabisat" )
else : 
    print (tahun,"bukan tahun kabisat")
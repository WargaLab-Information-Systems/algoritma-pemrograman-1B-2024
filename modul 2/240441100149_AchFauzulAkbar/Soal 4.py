# Soal No 4

tahun = int(input('masukan tahun : '))

if (tahun % 400 == 0):
    print('merupakan tahun kabisat')
elif (tahun % 100 == 0):
    print('bukan tahun kabisat')
elif (tahun % 4 == 0):
    print('merupakan tahun kabisat')
else:
    print('bukan tahun kabisat')
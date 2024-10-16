tahun = int(input("masukkan tahun"))
#tahun kabisat adalah tahun yang hanya muncul dalam 4 tahun sekali
# jika tahun tersebut habis dibagi 4 makan tahun tersebut merupakan tahun kabisat
# tahun akhir abad (berakhiran 00) harus habis dibagi 400
# jika tahun tersebut tidak habis dibagi 400 tapi habis dibagi 100 berarti bukan tahun kabisat 

if ( tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(tahun,"merupakan tahun kabisat.")
else:
    print(tahun,"bukan tahun kabisat")

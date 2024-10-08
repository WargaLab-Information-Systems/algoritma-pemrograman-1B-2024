#jika angka tahun habis dibagi 400, itu adalah tahun kabisat
#jika angka tahun habis dibagi 4, maka juga tahun kabisat
#jika tahun tahun habis dibagi 100, maka bukan tahun kabisat


tahunkabisat= int (input("masukan tahun = "))
if tahunkabisat%400==0:
    print(tahunkabisat,"tahun kabisat")
elif tahunkabisat%4==0:
    print(tahunkabisat, "termasuk juga tahun kabisat")
elif tahunkabisat%100==0:
    print(tahunkabisat, "bukan tahun kabisat")
else:
    print(tahunkabisat, "bukan tahun kabisat")


        
           
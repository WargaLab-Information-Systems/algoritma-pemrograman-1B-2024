tahun = int(input("masukkan tahunnya : "))
if tahun >=1500 :
    if tahun % 4 == 0 : #tahun yang habis dibagi 4 dan habis dibagi 400
        print(f"tahun{tahun} merupakan tahun kabisat")
    elif tahun % 100 == 0 and tahun % 400 == 0 : #tahun yang habis dibagi 100 tetapi tidak habis dibagi 400
        print(f"tahun {tahun} bukan tahun kabisat")
    else:
        print(f"{tahun} bukan tahun kabisat!!!")
   
else : 
    print(f"{tahun} bukan tahun kabisat!!!")
while True :
    angka = input("Masukkan angka bilangan bulat: ")
    angka_terbalik = angka[::-1]
    print("Angka setelah di balik: ",angka_terbalik)

    hitung_lagi = input("Apakah Anda ingin membalikkan angka lagi? (iya/tidak): ")
    if hitung_lagi != "iya":
       print("Terimakasih telah menyoba programku")
       break
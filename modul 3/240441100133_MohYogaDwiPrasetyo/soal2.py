while True:
    angka = input("Masukkan angka: ")
    
    # cek apakah angka pertama negatif
    if angka[0] == '-':
        negatif = True # tanda bahwa input adalah negatif
        angka = angka[1:] # hilangkan tanda negatif sementara
    else:
        negatif = False
    
    # balik angka
    balik_angka = "" # variabel kosong menyimpan hasil
    for i in angka:
        balik_angka = i + balik_angka # masukkan tiap digit di depan angka_balik
    
    if negatif:
        balik_angka = '-' + balik_angka # tambah "-" jika negatif
    
    print(f"Angka yang dibalik: {balik_angka}")
    break

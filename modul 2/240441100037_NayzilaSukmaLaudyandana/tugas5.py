nama = input("Masukkan nama pembeli: ")
member = input("Apakah memiliki kartu member? (ya/tidak): ")
total_belanja = float(input("Masukkan total belanja: Rp "))
usia = int(input("Masukkan usia pembeli: "))

if usia < 18:
    print("Maaf, usia Anda belum mencukupi.")
else:
    diskon = 0
    if member == "ya":
        diskon += 15
    if total_belanja > 500000:
        diskon += 10

    total_diskon = total_belanja * (diskon / 100)
    total_bayar = total_belanja - total_diskon

    
    print("Nama Pembeli:", nama)
    print("Diskon yang didapatkan:", diskon, "%")
    print("Total Harga Sebelum Diskon: Rp", total_belanja)
    print("Total Harga Setelah Diskon: Rp",total_bayar)

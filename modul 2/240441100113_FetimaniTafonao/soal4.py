nama_pembeli = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia: "))
total_belanja = float(input("Masukkan total belanja: "))
kartu_member = input("Apakah memiliki kartu member? (ya/tidak): ")

if usia < 18:
    print("Maaf, usia Anda belum mencukupi.")
else:
    diskon = 0
    if kartu_member == "ya":
        diskon += 15
    if total_belanja > 500000:
        diskon += 10

    total_diskon = total_belanja * diskon / 100
    total_bayar = total_belanja - total_diskon

    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga sebelum diskon: Rp {total_belanja}")
    print(f"Total harga setelah diskon: Rp {total_bayar}")
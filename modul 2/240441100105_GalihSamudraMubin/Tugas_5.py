nama_pembeli = input("Masukkan Nama Pembeli :")
usia_pembeli = int(input("Masukkan Usia Anda    :"))

if usia_pembeli < 18:
    print("Maaf Usia Anda Belum Mencukupi")
else:
    print("Selamat datang di Bar Kami, Mau Pesan Apa?")
    nama_minuman = input("Masukkan Nama Minuman Yang Ingin Anda Beli :")
    jumlah_pesanan = int(input("Masukkan Jumlah Yang Ingin Anda Pesan :"))
    harga_pesanan = int(input("Masukkan Harga Produk :"))
    total_belanja = jumlah_pesanan * harga_pesanan

    member = input("Apakah Anda Memiliki Kartu Member? (ya/tidak) :")
    
    diskon_member = 0
    diskon_total_belanja = 0

    if member == "ya":
        diskon_member = 15
    elif total_belanja >= 500000:
        diskon_total_belanja = 10

    if diskon_member > 0:
        total_diskon = diskon_member
    else:
        total_diskon = diskon_total_belanja

    total_setelah_diskon = total_belanja - (total_belanja * total_diskon / 100)

    print("----------------NOTA BELANJA----------------")
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang Didapatkan: {total_diskon}%")
    print(f"Total Harga Sebelum Diskon: Rp {total_belanja}")
    print(f"Total Harga Setelah Diskon: Rp {total_setelah_diskon}")
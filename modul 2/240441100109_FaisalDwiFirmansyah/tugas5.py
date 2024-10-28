nama_pembeli = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))

if usia < 18:
    print("Maaf, usia anda belum cukup.")
else:
    
    total_belanja =int(input("Masukkan total harga belanja: Rp. "))
    member = input("Apakah anda memiliki kartu member (ya/tidak)? ")

    if member == "ya" and total_belanja > 500000:
        diskon = 25
    elif total_belanja > 500000:
        diskon = 10
    elif member == "ya" :
        diskon = 15
    else:
        diskon = 0

    total_harga_setelah_diskon = total_belanja - (total_belanja * diskon / 100)

    print(f"\nNama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga sebelum diskon: Rp. {total_belanja: }")
    print(f"Total harga setelah diskon: Rp. {int(total_harga_setelah_diskon): }")
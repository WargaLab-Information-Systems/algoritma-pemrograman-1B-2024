
nama_pembeli = input("Masukkan nama pembeli: ")
usia_pembeli = int(input("Masukkan usia pembeli: "))


if usia_pembeli < 18:
    print("Maaf usia anda belum mencukupi.")

    
else:
    total_belanja = float(input("Masukkan total belanja: "))
    kartu_member = input("Apakah anda memiliki kartu member? (y/t): ")

    diskon = 0

    #cek punya member atau tdk
    if kartu_member == 'y':
        diskon = diskon + 15 

    #cek total belanja lebih dari 500.000 atau tidak jika iya dapat diskon tambahan 10%
    if total_belanja > 500000:
        diskon = diskon + 10  


    total_harga_sebelum_diskon = total_belanja

    #cek harga setelah diskon
    total_harga_setelah_diskon = total_harga_sebelum_diskon * (1 - (diskon / 100))


    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga sebelum diskon: Rp{total_harga_sebelum_diskon:}")
    print(f"Total harga setelah diskon: Rp{total_harga_setelah_diskon:}")

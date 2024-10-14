nama = (input("Masukkan nama pembeli : "))
harga_asli = int(input("Masukkan total pembelanjaan pembeli : "))
member = input("Apakah anda memiliki kartu member (ya/tidak)? ")
usia = int(input("Masukkan usia pembeli : "))

if usia <18:
    print("Maaf usia anda belulm mencukupi")
else:
    if member == "ya" and harga_asli > 500000:
        tot_harga = harga_asli - (harga_asli * 25/100)
        print(f"Nama pembeli adalah {nama}")
        print("Diskon yang didapat sebesar 25%")
        print(f"Harga sebelum diskon adalah {harga_asli}")
        print(f"Total harga setelah diskon adalah {tot_harga}")
    elif harga_asli >500000:
        tot_harga = harga_asli - (harga_asli * 10/100)
        print(f"Nama pembeli adalah {nama}")
        print("Diskon yang didapat sebesar 10%")
        print(f"Harga sebelum diskon adalah {harga_asli}")
        print(f"Total harga setelah diskon adalah {tot_harga}")
    elif member == "ya":
        tot_harga = harga_asli - (harga_asli * 15/100)
        print(f"Nama pembeli adalah {nama}")
        print("Diskon yang didapat sebesar 15%")
        print(f"Harga sebelum diskon adalah {harga_asli}")
        print(f"Total harga setelah diskon adalah {tot_harga}")
    else:
        print(f"Total harga anda adalah {harga_asli} ")
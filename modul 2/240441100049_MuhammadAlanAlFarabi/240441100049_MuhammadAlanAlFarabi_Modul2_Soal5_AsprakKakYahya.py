nama = str(input("Masukan Nama anda: "))
nim  = str(input("Masukan Nim anda: "))
usia = int(input("Silakan inputkan usia anda: "))


if usia >= 18:
    input("Apakah anda memiliki kartu member? bila punya mohon tekan enter, kemudian ketik ya. bila tidak tekan enter, ketik tidak")
    member = str(input())
    total = float(input("Tolong inputkan total belanja anda: "))
    if member == "ya":
        if total >= 500000:
            disk3 = total - total * (15 / 100 + 10 / 100)
            print("Nama adalah ", nama, "dengan Nim ", nim)
            print("sebelum diskon ", total)
            print("setelah diskon ", disk3)
        else:
            disk2 = total - total * 15 / 100
            print("Nama adalah ", nama, "dengan Nim ", nim)
            print("sebelum diskon ", total)
            print("sesudah diskon ", disk2)
    else:
        if total >= 500000:
            disk1 = total - total * 10 / 100
            print("Nama adalah ", nama, "dengan Nim ", nim)
            print("sebelum diskon ", total)
            print("sesudah diskon ", disk1)
        else:
            print("Nama adalah ", nama, "dengan Nim ", nim)
            print("anda tidak mendapat diskon sama sekali")
            print("total anda adalah", total)
else:
    print("anda di larang melakukan transaksi apa pun di sini")
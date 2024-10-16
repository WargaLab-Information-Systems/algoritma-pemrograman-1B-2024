denda_perhari = 2500
denda_tambahan = 5500
while True:
    hari = int(input("masukkan berapa lama kamu meminjam DVD:"))
    if hari > 5 and hari <= 10:
        print(f"denda yang harus dibayar = {float(denda_perhari * (hari - 5))}")
    elif hari > 10:

        keterlambatan = hari - 10
        total_denda_tambahan = (keterlambatan // 5) * denda_tambahan

        print(f"Denda yang harus dibayar = Rp. {float(denda_perhari * (hari - 5) + total_denda_tambahan)}")
    else:
        print("anda tidak perlu membayar denda")
    ulang = input("apakah anda mau menghitung kembali y/n:")
    if ulang == "n":
         print("terimakasih :)")
         break
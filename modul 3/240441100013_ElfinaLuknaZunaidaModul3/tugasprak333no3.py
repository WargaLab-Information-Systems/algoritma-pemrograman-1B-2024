denda_perhari = 2500
denda_tambahan = 5500
while True:
    hari = int(input("berapa lama kamu meminjam DVD:"))
    if hari > 5 and hari <= 10:
        print(f"denda yang harus dibayar = {float(denda_perhari * (hari - 5))}")
    elif hari > 10:

        keterlambatan = hari - 10
        denda_tambahan_total = (keterlambatan // 5) * denda_tambahan

        print(f"Denda yang harus dibayar = Rp. {float(denda_perhari * (hari - 5) + denda_tambahan_total)}")
    else:
        print("anda tidak perlu membayar denda")
    ulang = input("apakah anda mau menghitung ulang? ya/tidak:")
    if ulang == "tidak":
        print("terimakasih sudah meminjam DVD di tempat kami")
        break
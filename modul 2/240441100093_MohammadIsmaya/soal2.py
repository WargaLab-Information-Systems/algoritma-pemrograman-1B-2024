
nama = input("masukkan nama: ")
skor = int(input("masukkan skor: "))
ipk = float(input("masukkan ipk: "))

min_skor = int(input("masukkan minimal skor: "))
min_ipk = float(input("masukkan minimal ipk: "))


if skor >= min_skor and ipk >= min_ipk:
    print(nama, "lulus beasiswa dengan skor =", skor, "dan ipk =", ipk)
else:
    print(nama, "tidak lulus beasiswa dengan skor =", skor, "dan ipk =", ipk)
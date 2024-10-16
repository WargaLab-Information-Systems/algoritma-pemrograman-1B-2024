minimal_skor =1100
minimal_ipk = 3.0

nama = str(input ("masukkan nama :"))
skor = float(input ("masukkan skor :"))
ipk = float(input ("masukkan ipk :"))

if skor <= 1100 and ipk < 3.0:
    print(f"{nama} dinyatakan tidak lulus persyaratan beasiswa")
else:
    print(f"{nama} dinyatakan lulus persyaratan beasiswa")
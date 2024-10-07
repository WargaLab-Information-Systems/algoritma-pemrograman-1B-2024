hitung_kabisat = int(input("Masukkan tahun yang ingin dicek"))

if hitung_kabisat % 400 == 0 :
    print(hitung_kabisat,"adalah tahun kabisat.")
elif hitung_kabisat % 100 == 0 :
    print(hitung_kabisat, "bukan tahun kabisat.")
else:
    print(hitung_kabisat,"bukan tahun kabisat.")
# Diketahui Data Mahasiswanya
cowo = "Jaka"
skor_cowo = 1100
ipk_cowo = 3.5

cewe = "ida"
skor_cewe = 1000
ipk_cewe = 3.5

# Syarat Kelulusan
skor_minimum = 1100
ipk_minimum = 3.0

# Mari kita cek kelulusan jaka
if skor_cowo >= skor_minimum and ipk_cowo >= ipk_minimum:
    print(f"{cowo} Lulus Persyaratan Beasiswa.")
else:
    print(f"{cowo} Tidak Lulus Persyaratan Beasiswa.")

# Dan sekarang kita cek kelulusan ida
if skor_cewe >= skor_minimum and ipk_cewe >= ipk_minimum:
    print(f"{cewe} Lulus Persyaratan Beasiswa.")
else:
    print(f"{cewe} Tidal Lulus Persyaratan Beasiswa.")

# Data yang diketahui di soal
Total = 7 #jumlah total orang(n)
Terpilih = 4 #terpilih(r)
sisa = 3 #sisa

# Hitung menggunakan kombinasi
# Rumus C(n,r)=7!/4!(7-4)!
Total = 7*6*5*4*3*2*1
Terpilih = 4*3*2*1
sisa = 3*2*1
print(f"{Total} : ({Terpilih}x{sisa})")
k = Terpilih*sisa
print(f"{Total} : {k}")
kombinasi = (Total / (k))
# Hasil kombinasi
print(f"Banyak cara Darsono membentuk tim: {kombinasi} cara")
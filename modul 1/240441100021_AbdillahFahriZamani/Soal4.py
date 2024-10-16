# Diket ada 7 orang sedangkan yang mau dipilih darsono adalah 4 orang untuk masuk kedalam timnya

# Input jumlah total orang dan jumlah orang yang ingin dipilih
orang = int(input("Jumlah total orang: "))
dipilih = int(input("Jumlah orang yang dipilih: "))

n = orang
r = dipilih

# Menghitung kombinasi
import math
if r <= n:
    jumlah = math.comb(n, r)
    print(f"Cara memilih {r} dari {n} orang: {jumlah}")
else:
    print("Jumlah orang yang dipilih tidak boleh lebih dari total orang.")
#C n,r = n! / (r!.(n-r)!)
#comb 7,4 = 7! / (4!.(7-4)!)


# data yang ada disoal
n = 7 #total jumlah orang
r = 4 #jumlah orang yang ingin dipilih
c = 3

faktorial_n = 7 * 6 * 5 * 4 * 3 * 2 * 1
faktorial_r = 4 * 3 * 2 * 1
faktorial_c = 3 * 2 * 1
print(faktorial_n)
print(faktorial_r)
print(faktorial_c)

# menghitung banyak cara untuk memilih 4 orang dari 7 orang
kombinasi = faktorial_n / (faktorial_r * faktorial_c)
print(f"Banyak cara untuk membentuk tim yang akan disusun oleh Darsono adalah {kombinasi} cara")

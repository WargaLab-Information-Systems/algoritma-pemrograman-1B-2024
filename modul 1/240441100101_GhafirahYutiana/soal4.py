# menggunakan rumus kombinasi C(n, r) = n!/ (r! * (n - r) !)
# Declare Variabel
n = 7 # total orang
r = 4 # jumlah orang dalam tim
faktorial_7= 7*6*5*4*3*2*1
faktorial_4= 4*3*2*1
faktorial_3= 3*2*1

# Rumus mencari jumlah cara untuk memilih tim
jumlah_cara = (faktorial_7) / (faktorial_4 * faktorial_3)
print(F"jumlah cara membentuk tim tim:{jumlah_cara}")
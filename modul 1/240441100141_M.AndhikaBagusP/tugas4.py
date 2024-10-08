# Input data
n = 7 #Total orang
r = 4 #Orang dipilih
b = 3 #Tidak terpilih (n-r)

#mencari faktorial 
faktorial_n = 7*6*5*4*3*2*1
faktorial_r = 4*3*2*1 
faktorial_b = 3*2*1

# Hitung banyaknya kombinasi
kombinasi = faktorial_n / faktorial_r * faktorial_b
hasil = kombinasi

# hasil
print(f"Jadi, Ada {hasil} cara untuk membantuk tim")    
#pertama-tama mari kita faktorialkan semua
faktorial_n= 7*6*5*4*3*2*1 #nilai   n=7
print("jumlah 7! adalah", faktorial_n)
faktorial_r= 4*3*2*1       #nilai   b=4
print("jumlah 4! adalah", faktorial_r)
faktorial_d=3*2*1          #nilai n-r=3
print("jumlah 3! adalah", faktorial_d)
print("kombinasi = " "\nn!/r!*n-r!")
print("5040/24*6 =")
kombinasi=faktorial_n / faktorial_r * faktorial_d
print(int(kombinasi))

# START

# // Diketahui
# faktorial_n ← 7 * 6 * 5 * 4 * 3 * 2 * 1   // n = 7
# faktorial_r ← 4 * 3 * 2 * 1               // r = 4
# faktorial_d ← 3 * 2 * 1                   // n - r = 3

# // Menghitung kombinasi
# kombinasi ← faktorial_n / (faktorial_r * faktorial_d)

# // Menampilkan hasil
# PRINT kombinasi

# END
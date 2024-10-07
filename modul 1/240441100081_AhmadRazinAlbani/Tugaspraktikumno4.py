#no4
#MENGHITUNG BANYAK CARA DALAM MEMBENTUK TIM

import math
# data yang ada disoal
n = 7 #total jumlah orang
r = 4 #jumlah orang yang ingin dipilih

# menghitung banyak cara untuk memilih 4 orang dari 7 orang
def kombinasi(n, r): 
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
hasil = kombinasi(n, r)
print(f"Banyak cara untuk membentuk tim yang akan disusun oleh Darsono adalah {hasil} cara")

import math

def hitung_kombinasi(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

n = 7
k = 4
hasil = hitung_kombinasi(n, k)
print(f"Ada {hasil} cara membentuk tim {k} orang dari total {n} orang.")
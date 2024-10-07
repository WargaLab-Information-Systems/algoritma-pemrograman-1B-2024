# Menghitung banyak cara untuk membentuk tim

#Menggunakan rumus faktorial c(n,k) = n! / k! (n!-k!)
import math
n = 7
k = 4

m = (n-k)
c = int(math.factorial (n) / (math.factorial(k)*math.factorial(m)))
print("Jadi, banyak cara untuk membentuk tim tersebut adalah ", c, "cara")
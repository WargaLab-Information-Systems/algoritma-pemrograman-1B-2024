#program menghitung cara untuk membentuk tim
print("PROGRAM MENGHITUNG CARA MENGHITUNG TIM")

# DIKETAHUI
# n = total tim sebelum ditambah
# r = jumlah yang ingin ditambah
# c (n, r)

#menggunakan rumus kombinasi

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

print (faktorial(7))
print (faktorial(4))

def kombinasi(n, r):
    return faktorial(n) / (faktorial(r) * faktorial(n - r))

#jumlah tim dan memilih orang
n = 7
r = 4
banyaknya_cara = kombinasi(n, r)

print(f"hasil dari menghitung banyak cara dengan tim {n} orang dan memilih {r} orang adalah: {banyaknya_cara} ", "orang" )
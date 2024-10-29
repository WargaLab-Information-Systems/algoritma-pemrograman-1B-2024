# nested loop / looping bersarang

# for i in range (1,4):
#     print(f"loop luar i = {i}")
#     for j in range (1,4):
#         print(f"loop dalam j = {j}")

# for i in range (5):
#     for j in range (6):
#         print(f"[", i,j, "]", end=" ")
#     print()

# struktur pengulangan kombinasi
a = 24
b = 36

# while b !=0:
#     a,b = b,a%b

# print(f"faktor persekutuan terbesar adalah: {a}")

# nilai = input("masukkan nilai : ")
# for i in range (1, 10+1):
#     hasil = i * nilai
#     print(nilai, "*", i, "=", hasil)

# Deret Fibonacci 
# n = 100
# a, b = 0, 1

# print("Bilangan Fibonacci hingga", n)
# while a <= n :
#     print(a, end=" ")
#     a, b = b, a+b

n = 5 
for i in range (1, n+1):
    for j in range (n-i):
        print(' ', end= ' ')
    for k in range (1, i+1):
        print(k, end=' ')
    print()

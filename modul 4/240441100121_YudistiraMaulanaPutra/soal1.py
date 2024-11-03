# 1 sssss* 
# 2 ssss* *
# 3 sss* * *
# 4 ss* * * *
# 5 s* * * * *
#   ss* * * *
#   sss* * *
#   ssss* *
#   sssss* 
n = int(input("Masukkan N: "))
k = str(input("Masukkan karakter: "))
for i in range(n):
    print(" " * (n - i) + (k + " ") * (i + 1))
for i in range(1,n):
    print(" " * (i + 1) + (k + " ") * (n - i))
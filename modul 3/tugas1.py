n = int(input("Masukkan size : "))

# # untuk 0
for i in range(n):
    if i == 0 or i == n - 1 :
        print("x"*n)
    else: 
        print("x"+" "*(n-2)+"x")

print()
 
# # untuk 5
for i in range(n):
    if i == 0 or i == n // 2 or i == n - 1 :
        print("x"*n)
    elif i < n // 2:  
        print("x") 
    else:
        print(" "*(n-1)+"x") 

print()

# untuk 7
for i in range(n):
    if i == 0 :
        print("x"*n)
    else:
        print(" "*(n-i-1)+"x")

print()
 
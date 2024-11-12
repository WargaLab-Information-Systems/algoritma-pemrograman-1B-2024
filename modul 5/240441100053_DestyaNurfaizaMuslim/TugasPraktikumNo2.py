# fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci (n-2)
    
n = int(input("Masukkan bilangan bulat non negatif : "))
if n >= 0:
    print("Bilangan fibonacci ke-", n, "adalah", fibonacci(n))
else:
    print("Masukkan bilangan bulat non negatif")
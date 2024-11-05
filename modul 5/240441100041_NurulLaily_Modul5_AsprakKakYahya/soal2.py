def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input("Masukkan bilangan non-negatif: "))

if n < 0:
    print("Harapkan masukkan bilangan non-negatif.")
else:
    print(f"Bilangan Fibonacci ke-{n} adalah {fibonacci(n)}")
    
def tampil():
    print("Hallo dunia")
    c = 5
    print(c)
    
    
tampil()
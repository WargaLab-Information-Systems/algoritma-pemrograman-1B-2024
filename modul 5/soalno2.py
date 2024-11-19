def fibonacci(n):
    # Basis rekursi
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Rekurens untuk menghitung Fibonacci
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Masukkan nilai n: "))

if n < 0:
    print("Masukkan nilai positif!")
else:
    print("Bilangan Fibonacci ke-", n, "adalah:", fibonacci(n))

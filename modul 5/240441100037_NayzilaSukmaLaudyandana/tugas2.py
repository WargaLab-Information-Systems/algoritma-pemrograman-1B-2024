def fibonacci(n):
    if n <= 1:
        return n
    else:
        hasil = fibonacci(n - 1) + fibonacci(n - 2)
        return hasil


n = int(input("Masukkan Angka: "))
print("Bilangan Fibonacci ke ",n," adalah ", fibonacci(n))
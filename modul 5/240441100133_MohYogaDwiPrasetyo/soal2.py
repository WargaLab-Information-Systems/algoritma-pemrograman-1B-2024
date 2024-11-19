def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Masukkan nilai n: "))
if n < 0:
    print("Masukkan bilangan non-negatif!")
else:
    hasil = fibonacci(n)
    print(f"Fibonacci ke-{n} adalah: {hasil}")
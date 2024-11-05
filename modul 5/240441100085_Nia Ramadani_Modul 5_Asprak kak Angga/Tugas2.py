def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Masukkan nilai n: "))
print(f"Bilangan Fibonacci ke-{n} adalah {fibonacci(n)}")


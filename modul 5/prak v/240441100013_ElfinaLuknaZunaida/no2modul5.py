def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Masukkan bilangan untuk menghitung Fibonacci ke-n: "))
print(f"Fibonacci ke-{n} adalah {fibonacci(n)}")


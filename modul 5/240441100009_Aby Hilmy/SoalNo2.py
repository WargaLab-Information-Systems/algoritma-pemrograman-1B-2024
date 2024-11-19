def fibonacci(n):
    # Basis kasus: jika n adalah 0 atau 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Panggilan rekursif untuk menghitung fibonacci(n-1) dan fibonacci(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("masukkan nilai n:"))
print(f"Bilangan Fibonacci ke-{n} adalah {fibonacci(n)}")

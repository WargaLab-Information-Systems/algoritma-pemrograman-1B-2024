def fibonacci(n):
    # Basis kasus
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Rekursi
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    n = int(input("Masukkan nilai n untuk menghitung Fibonacci ke-n: "))
    if n < 0:
        print("Masukkan nilai positif.")
    else:
        print(f"Fibonacci ke-{n} adalah {fibonacci(n)}")
except ValueError:
    print("Masukkan angka yang valid.")
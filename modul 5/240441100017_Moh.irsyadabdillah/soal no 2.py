def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1: 
        return 1
    # Rekursi: kembalikan penjumlahan fibonacci(n-1) dan fibonacci(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Masukkan bilangan bulat non-negatif: "))
print(f"Bilangan Fibonacci ke-{n} adalah {fibonacci(n)}")

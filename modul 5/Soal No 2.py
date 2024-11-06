def fibonacci(n):
    # Cek jika n adalah 0 atau 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Panggilan rekursif untuk menghitung fibonacci(n-1) dan fibonacci(n-2)

# Contoh penggunaan
n = int(input("Masukkan bilangan bulat non-negatif: "))
if n < 0:
    print("Silakan masukkan bilangan bulat non-negatif.")
else:
    print(f"Fibonacci ke-{n} adalah: {fibonacci(n)}")
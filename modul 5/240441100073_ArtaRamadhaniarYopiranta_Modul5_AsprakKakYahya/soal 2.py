def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Masukan bilangan bulat non negatif n: "))
if n < 0:
    print("Bilangan bulat harus positif.")
else:
    hasil = fibonacci(n)
    print(f"Bilangan Fibonacci ke-{n} adalah {hasil}")
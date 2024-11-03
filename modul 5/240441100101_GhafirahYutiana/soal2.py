def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    n = int(input("Masukkan nilai n harus bilangan bulat non-negatif: "))
    if n >= 0:
        print(f"Bilangan Fibonacci ke-{n} adalah {fibonacci(n)}")
        break
    else:
        print("input tidak valid. Silahkan masukkan bilangan bulat non-negatif")
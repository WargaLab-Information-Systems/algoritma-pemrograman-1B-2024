def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Masukkan bilangan Fibonacci: "))
if n < 0:
    print("angka harus positif!!")
else:
    print(f"Bilangan Fibonacci ke-{n} adalah: {fibonacci(n)}")
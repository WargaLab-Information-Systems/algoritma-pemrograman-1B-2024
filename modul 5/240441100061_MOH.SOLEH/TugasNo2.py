# Buat fungsi rekursif fibonacci(n) yang menerima parameter bilangan bulat non-negatif
# dan mengembalikan nilai Fibonacci ke-n. dan Gunakan rekursi untuk menghitungnya.

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input("Masukkan nilai n : "))
if n < 0:
    print("Masukkan bilangan bulat non-negatif.")
else:
    print(f"Bilangan Fibonacci ke-{n} adalah : {fibonacci(n)}")
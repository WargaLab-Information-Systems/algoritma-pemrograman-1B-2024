def fibonacci(angka):
    # Basis kasus: jika n adalah 0 atau 1
    if angka == 0:
        return 0   #mengirimkan nilai
    elif angka == 1:
        return 1
    else:
        # Rekursi: fibonacci(angka) = fibonacci(angka-1) + fibonacci(angka-2)
        return fibonacci(angka - 1) + fibonacci(angka - 2)

# Meminta input dari pengguna
try:
    angka = int(input("Masukkan bilangan bulat non-negatif untuk menghitung Fibonacci: "))
    if angka < 0:
        print("Silakan masukkan bilangan bulat non-negatif.")
    else:
        print(f"Fibonacci ke-{angka} adalah {fibonacci(angka)}")
except ValueError:
    print("Input tidak valid. Harap masukkan bilangan bulat non-negatif.")
    

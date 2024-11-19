def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n):
            print(a, "+", b)
            a, b = b, a + b
        return a


# Meminta input dari pengguna
while True:
    try:
        n = int(input("Masukkan bilangan bulat non-negatif untuk menghitung Fibonacci: "))
        if n < 0:
            print("Silakan masukkan bilangan bulat non-negatif.")
        else:
            print(f"Fibonacci ke-{n} adalah {fibonacci(n)}")
            break

    except ValueError:
        print("Input tidak valid. Silakan masukkan bilangan bulat.")

    ulang = input("apakah anda ingin mengulang? y/n : ")
    if ulang != "y" :
        print("terima kasih")
        break
    else:
        print()
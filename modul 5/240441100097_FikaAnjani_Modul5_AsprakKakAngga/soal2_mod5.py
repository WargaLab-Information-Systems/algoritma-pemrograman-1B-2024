def fibonacci (n):
    if n == 0:
        return[n]
    
    angka = fibonacci(n-1)
    indek = len(angka)

    angka1 = angka[-2] if indek > 2 else 0
    angka2 = angka[-1] if indek > 2 else 1
    return angka + [angka1 + angka2]

angka_fib = int(input("masukkan angka :"))
print(fibonacci(angka_fib-1))
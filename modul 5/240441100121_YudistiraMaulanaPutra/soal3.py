def faktorial(n):
    hasil = 1
    for i in range(1, n):
        hasil *= i
    return hasil
n = int(input("Masukkan bilangan bulat: "))
print(f"{n}! = {faktorial(n)}")
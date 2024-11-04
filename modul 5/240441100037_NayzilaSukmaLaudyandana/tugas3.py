def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan Angka : "))

proses = " x ".join(str(i) for i in range(n, 0, -1))
print(f" {n}!= ", proses,"=", faktorial(n))
    
    
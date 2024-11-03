def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        hasil = n
        proses = f"{n}"
        for i in range(n - 1, 0, -1):
            hasil *= i
            proses += f"x{i}"
        print(f"{n}! = {proses} = {hasil}")
        return hasil

n = int(input("Masukkan nilai n: "))
faktorial(n)

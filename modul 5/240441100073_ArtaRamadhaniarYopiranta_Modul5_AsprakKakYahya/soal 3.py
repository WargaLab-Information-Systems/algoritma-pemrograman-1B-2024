def faktorial(n):
    if n == 0 or n == 1:
        print(f"{n}! = 1")
        return 1
    
    hasil = 1
    proses = f"{n}! = "

    for i in range (n, 0, -1):
        hasil *= i
        proses += f"{i} x " if i > 1 else f"{i} = {hasil}"

    print(proses)
    return hasil

n = int(input("Masukan bilangan untuk dihitung faktorialnya: "))
faktorial(n)
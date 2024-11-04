
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n*faktorial(n-1)
    
def tampilkan_proses(n):
    proses = ""
    for i in range(n,0,-1):
        if i > 1:
            proses += (f"{i}*")
        else:
            proses += (f"{i}")
    return proses

n = int(input("Masukkan bilangan bulat positif: "))
hasil = faktorial(n)
proses = tampilkan_proses(n)

print(f"Nilai faktorial dari {n}! = {proses} = {hasil}")
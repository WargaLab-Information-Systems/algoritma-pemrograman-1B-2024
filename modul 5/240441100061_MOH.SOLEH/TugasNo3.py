# Membuat fungsi untuk menghitung faktorial suatu bilangan

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    # Rekursif
    else:
        return n * faktorial(n - 1)
bilangan = int(input("Masukkan bilangan : "))
if bilangan < 0:
    print("Tolong masukkan bilangan bulat non negatif.")
else:
    hasil = faktorial(bilangan)
    print(f"{bilangan}! = {hasil}")

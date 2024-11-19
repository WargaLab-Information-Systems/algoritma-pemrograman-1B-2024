def faktorial(n):
    # Basis rekursi
    if n == 0:
        return 1
    # Rekurens untuk menghitung faktorial
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan nilai n: "))

if n == 0:
    hasil_perhitungan = "1"
else:
    hasil_perhitungan = ""
    for i in range(n, 0, -1):
        hasil_perhitungan += str(i) 
        if i > 1:
            hasil_perhitungan += " x "

hasil = faktorial(n)
print(f"{n}! = {hasil_perhitungan} = {hasil}")

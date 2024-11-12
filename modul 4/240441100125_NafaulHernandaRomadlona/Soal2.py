
hasil_biner = ""
n = int(input("Masukkan bilangan : "))

while n > 0:
    hasil_bagi_sisa = n % 2
    hasil_biner = str(hasil_bagi_sisa) + hasil_biner
    n = n // 2

# Tampilkan pola segitiga
for i in range(1, len(hasil_biner) + 1):
    print(hasil_biner[:i])
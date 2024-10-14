angka = int(input("Masukkan angka: "))
angkaTerbalik = 0

while angka != 0:
    digit = angka % 10 
    angkaTerbalik = angkaTerbalik * 10 + digit
    angka = angka // 10

print(f"Angka setelah dibalik {angkaTerbalik}: ")
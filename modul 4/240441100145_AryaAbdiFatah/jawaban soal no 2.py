n = int(input("masukan nilai desimal: "))
s = ""
while n > 0:
    r = n % 2 
    s = str(r) + s # s yang baru + s yang lama
    print(s)
    n = n // 2 #tugas n untuk memperbarui n>0


# // = 1 // 2 = 0, 5 di bulatkan kebawah menjadi 0 pemabgian yang dibulatkan ke bawah
# % = 1 % 2 = 1 dibagi 2 adalah 0 sisa (1 modulus (sisa hasil bagi))
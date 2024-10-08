nama = input("Masukkan nama anda= ")
usia = int(input("Berapakah usia anda?= "))

if usia >= 18:
    member = str(input("Apakah anda memiliki member?(y/n):= ")) .lower()
    if member == 'y':
        total = int(input("Berapakah total pembelian anda?= "))
        if total >= 500000:
            diskon2 = (float(15) / 100 + float(10) / 100) * total
            hdiskon2 = total - diskon2
            print("hasil diskon adalah" + str(hdiskon2))
            print(nama)
        else:
            diskon1 = float(15) / 100 * total
            hdiskon1 = total - diskon1
            print("hasil diskon adalah" + str(hdiskon1))
            print(nama)
    else:
        total = int(input("Berapakah total pembelian anda?= "))
        # tidak dapat diskon member
        if total >= 500000:
            diskon = total * 10/100
            Hdiskon = total - diskon
            print("hasil diskon adalah" + str(Hdiskon))
            print(nama)
        else:
            print("maaf tidak mendapatkan diskon" + str(total))
            print(nama)
else:
    print("maaf umur anda belum mencukupi")

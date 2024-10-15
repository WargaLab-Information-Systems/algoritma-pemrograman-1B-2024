# Pemberian diskon

nama = input("Siapa nama anda? ")
kartu = input("Apakah anda memiliki kartu member? ")
umur = int(input("Berapakah umur anda? "))
jumlah = int(input("Berapa total belanjaan anda? "))
print("======================")

print("Nama anda adalah", nama)

if umur < 18:
    print("Maaf usia anda belum mencukupi")
else:
    print("Total belanjaan anda adalah Rp.", jumlah)
    if  ((kartu == "iya") or (kartu == "ya")) :
        a = jumlah - (15/100*jumlah)
        print("Anda mendapatkan diskon 15% karena memiliki kartu member")
        print("Jadi, total belanjaan anda adalah Rp.", int(a))
    if  (jumlah > 500000) :
        b = jumlah - (10/100*jumlah)
        print("Anda mendapatkan diskon 10% karena belanja diatas Rp. 500000 ")
        print("Jadi, total belanjaan anda adalah Rp.", int(b)) 
    if ((kartu == "iya") or (kartu == "ya")) and (jumlah > 500000):
        c = jumlah - (25/100*jumlah)
        print()
        print("Selamat, anda mendapatkan total diskon 25% karena memiliki kartu member dan belanja diatas Rp. 500000 ")
        print("Jadi, total belanjaan anda semuanya adalah Rp.", int(c)) 



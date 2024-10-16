nama = str(input("masukkan nama :"))
umur = int(input("Masukkan umur anda :"))
if umur >= 18 :
    
    member = ("15%")
    belanja = ("10%")
    punya_member= str(input("Apakah kamu punya kartu member? (yes/no)"))
    jumlah_belanja = int(input("Berapa total belanja kamu?"))
    discount1 = 0
    discount2 = 0
    if punya_member == "yes" :
     discount1 = 15
    else:
        discount1 = 0

    if jumlah_belanja > 500000:
        discount2 = 10
    else:
        discount2 = 0
    total_discount = jumlah_belanja * (discount2 + discount1) / 100
    total_harga = jumlah_belanja - total_discount
    print(nama)
    print("discoun yang anda dapatkan adalah", total_discount)
    print("total harga sebelum diskon =", jumlah_belanja)
    print("total harga setelah diskon adalah ", total_harga)
else :
    print("maaf umur anda belum cukup")

   
   




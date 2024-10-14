nama = input("Masukkan nama customer ")
usia = int(input("Masukkan usia customer "))

# seleksi kondisi
if usia < 18:
    print("Maaf usia anda belum mencukupi")
else:
    totalbelanja = int(input("Total belanja anda adalah Rp. "))
    member = input("Apakah Anda memiliki memeber ('yes' / 'no'): ")

    if member == "yes":
        diskon_member = (15 / 100) * totalbelanja
    else:
        diskon_member = 0  
    
    if totalbelanja > 500000:
        diskon2 = (10 / 100) * totalbelanja
    else:
        diskon2 = 0

    # Diskon yang didapatkan
    total_diskon = diskon_member + diskon2

    # Harga setelah diskon
    harga_setelah_diskon = totalbelanja - total_diskon 

    print("Nama Customer:" ,nama) 
    print("Diskon yang didapatkan adalah" ,total_diskon)
    print("Harga sebelum diskon" ,totalbelanja)
    print("Harga sesudah diskon" ,harga_setelah_diskon)


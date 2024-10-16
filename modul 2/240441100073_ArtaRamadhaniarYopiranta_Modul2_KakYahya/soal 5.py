#data pembeli
nama = str(input("Masukan nama pembeli: "))
usia = int(input("Masukan usia pembeli: "))
total = float(input("Masukan total harga belanja pembeli: "))
kartu_member = input("Punya kartu member? (ya/tidak): ")

diskon_kartu_member = 0.15 * total
diskon_total_belanja = 0.10 * total
total_diskon = diskon_kartu_member + diskon_total_belanja
total_harga_setelah_diskon = total - total_diskon
total_harga_setelah_diskon_kartu_member = total - diskon_kartu_member
total_harga_setelah_diskon_total_belanja = total - diskon_total_belanja

if usia <= 18 :
    print("Maaf, usia anda tidak mencukupi")

else: 
    print("nama pembeli: ", nama)
    if kartu_member == 'ya' and total >= 500000:
        print("Diskon yang didapat pembeli: ", total_diskon)
        print("Harga sebelum diskon: ", total)
        print("Total harga setelah mendapatkan diskon: ", total_harga_setelah_diskon)
    elif kartu_member == 'ya': 
        print("Diskon yang didapat pembeli: ", diskon_kartu_member)
        print("Harga sebelum diskon: ", total)
        print("Total harga setelah mendapatkan diskon: ", total_harga_setelah_diskon_kartu_member)
    elif total >= 500000:
        print("Diskon yang didapat pembeli: ", diskon_total_belanja)
        print("Harga sebelum diskon: ", total)
        print("Total harga setelah mendapatkan diskon: ", total_harga_setelah_diskon_total_belanja)  
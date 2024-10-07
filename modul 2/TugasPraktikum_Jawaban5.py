nama = input("Nama Pembeli = ")
usia = int(input("Usia Pembeli = "))
total_belanja = float(input ("Masukan total belanja andah = Rp "))
punya_member = input("Apakah anda mempunyai kartu member? (iya/tidak) ")

if usia <= 18:
    print("Maaf usia anda belum mencukupi")
else:
    print("nama pembeli : ", nama)
    if punya_member == "iya"and total_belanja >= 500000:
        diskon_15 = (15/100)*total_belanja
        diskon_10 = (10/100)*total_belanja
        diskon_total = diskon_10+diskon_15
        total_harga_setelah_diskon_15dan10 = total_belanja-diskon_total
        print("Diskon yang didapat : ", diskon_total )
        print ("harga sebelum diskon : " , total_belanja)
        print("total harga setelah diskon : " , total_harga_setelah_diskon_15dan10)
    elif punya_member == "iya":
        diskon_15 = (15/100)*total_belanja
        total_harga_setelah_diskon_15 = total_belanja-diskon_15
        print("Diskon yang didapat : ", diskon_15)
        print ("harga sebelum diskon : ",total_belanja)
        print("total harga setelah diskon : " , total_harga_setelah_diskon_15)
    elif total_belanja >= 500000:
        diskon_10 = (10/100)*total_belanja
        total_harga_setelah_diskon_10 = total_belanja-diskon_10
        print("Diskon yang didapat : ", diskon_10)
        print ("harga sebelum diskon : ", total_belanja)
        print("total harga setelah diskon : ", total_harga_setelah_diskon_10)  
    else:
        print("Total belanja anda : ",total_belanja)

print("Terimakasih telah berkunjung di Bar kami.")  
waktuTempuhSaya = 0
waktuTotalKeKampus = 50
waktuMakan = 10
waktuMandi = 15
waktuMotor = 15
waktuJalanKaki = 30
print("SELAMAT DATANG DI SEMANGAT NGAMPUS CODE!!!!")

cek = input("Apakah kamu sudah makan atau mandi hari ini? (yes/no): ")
saya = "mahasiswa"

if cek == 'no':
    waktuTotalKeKampus -= waktuMakan
    waktuTotalKeKampus -= waktuMandi
    totalWaktu = waktuTotalKeKampus
    print(f"Waktu ke kampus anda hilang {waktuMakan} menit untuk makan dlu")
    print(f"Waktu ke kampus anda hilang {waktuMandi} menit untuk mandi dulu")
    print(f"Anda punya sisa waktu ke kampus {totalWaktu}")
else:
    if cek == 'yes':
     trans = input("Mau naik apa ke kampus? (motor/jalanKaki): ")
    if trans == 'motor':
        waktuTotalKeKampus -= waktuMotor
    if trans == 'jalanKaki':
        waktuTotalKeKampus -= waktuJalanKaki

print(f"total sisa Waktu {waktuTotalKeKampus}")




# if 2x
# if 1
# mandi dan makan adalah no maka waktu 
# dikurangi untuk makan dan minum total 50 - 25 = 25

# if 2





# `trans = str(input("Ok kalo gitu, Mau Naik apa cuy ke kampus?:(motor/jalanKaki) "))
# if trans == 'motor':
#     waktuTotalKeKampus -= waktuMotor
# if trans == 'jalanKaki':
#     waktuTotalKeKampus -= waktuJalanKaki


    
    


# print(f"sisa waktu ke kampus {waktuTotalKeKampus}")
# print(f"sisa waktu saya {waktuTempuhSaya}")

# makan = 0
# mandi = 0
# mengecek = 0 
# transportasi = 0
# waktu = 0
# #Mentukan apakah kamu berangkat 
# # tepat waktu atau terlambat berdasarkan perhitungan waktu tersebut
# waktuMaksimal = 60
# print(saya)

# if saya != makan:
#     waktu += 15 
#     print("Makan dulu cik")

# elif saya == makan:
#     pass
# if saya == mandi:
#     mandi += 10
#     mandi += 10
#     pass
# jalanKaki = 0
# motor = 0
# if saya == transportasi:
#    if transportasi == jalanKaki:
#     pass
#     waktu = 30
#     pass
#    if transportasi == motor: 
#     waktu = 15
#     pass
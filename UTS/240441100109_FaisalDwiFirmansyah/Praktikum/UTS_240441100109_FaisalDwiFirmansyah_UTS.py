makan = str(input("Apakah sudah melakukan makan (ya/tidak)? "))
mandi = str(input("Apakah kamu mandi (ya/tidak)? "))
pilihan_transportasi = input("Masukkan pilihan transportasi (motor/sepeda/jalankaki)? ")
belum_makan = 15
belum_mandi = 15
motor = 15
sepeda = 15

#Kasus 1
if makan == 'tidak':
    print("kamu belum makan")
else:
    print("Kamu sudah makan")

if mandi == 'ya':
    print("kamu sudah mandi")
else:
    print("Kamu belum mandi")

if pilihan_transportasi == 'motor':
    print("Kamu menggunakan motor")
else:
    print("Kamu menggunakan transportasi lain")

total_waktu = belum_makan + motor
print("Total waktu persiapan dan perjalanan kamu adalah", total_waktu, ("menit, dan kamu berangkat tepat waktu"))

#Kasus 2
# if makan == 'tidak':
#     print("kamu belum makan")
# else:
#     print("Kamu sudah makan")

# if mandi == 'tidak':
#     print("kamu sudah mandi")
# else:
#     print("Kamu belum mandi")

# if pilihan_transportasi == 'sepeda':
#     print("Kamu menggunakan sepeda")
# else:
#     print("Kamu menggunakan transportasi lain")

# total_waktu = belum_makan + sepeda
# print("Total waktu persiapan dan perjalanan kamu adalah", total_waktu, menit)








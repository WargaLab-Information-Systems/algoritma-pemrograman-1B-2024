tanya = str(input("apakah kamu sudah makan?  ya/tidak:"))
tanya2 = str(input("apakah kamu sudah mandi? ya/tidak:"))
makan = 15
mandi = 10

if tanya == 'tidak' :
    print(f"kamu harus makan dulu dengan waktu {makan}menit" )
    if tanya2 == 'tidak':
        print(f"kamu harus mandi dulu dengan waktu {mandi} menit")
else:
    print("kamu bisa lanjut")

jalan_kaki = 30
naik_motor = 15
tanya3 = str (input("kamu mau milih kendaraan apa? jalankaki/naikmotor:"))
tanya4 = str (input("kamu mau milih kendaraan apa? jalankaki/naikmotor:"))
if tanya3 == 'jalankaki':
    print(f"waktu yang kamu butuhkan ke kampus adalah {jalan_kaki} menit")
    if tanya4== 'naikmotor':
        print(f"waktu yang kamu butuhkan ke kampus adalah {naik_motor} menit")
else:
    print("kamu bisa lanjut")

#menghitung total waktu yang diperlukan untuk ke kampus
waktu_yang_tepat = 60

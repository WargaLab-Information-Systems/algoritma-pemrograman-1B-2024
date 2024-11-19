waktu_makan = 15
waktu_mandi = 10
waktu_jalankaki = 30
waktu_motor = 15
max_waktu = 60

makan = input("Apakah kamu sudah makan? (ya/tidak): ")
mandi = input("Apakah kamu sudah mandi? (ya/tidak): ")

waktu_persiapan = 0
if makan.lower() != "ya":
    waktu_persiapan += waktu_makan
if mandi.lower() != "ya":
    waktu_persiapan += waktu_mandi

transportasi = input("Pilih transportasi (jalan kaki/motor): ")

waktu_perjalanan = 0
if transportasi.lower() != "jalan kaki":
    waktu_perjalanan += waktu_jalankaki
else :
    waktu_perjalanan += waktu_motor

total_waktu = waktu_persiapan + waktu_perjalanan

total_waktu = 0
if total_waktu <= max_waktu :
    print("Total waktu yang dibutuhkan : [total_waktu] menit")
else :
    print("Total waktu yang dibutuhkan : [total_waktu menit")
    print("Kamu terlambat!")
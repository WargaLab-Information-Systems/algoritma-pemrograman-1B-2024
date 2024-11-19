
waktu_persiapan_awal = 0
waktu_makan = 15
waktu_mandi = 10
waktu_jalankaki = 30
waktu_pakaimotor = 15
maksimal_sampai = 50

#makan mandi
makan = input ("Apakah kamu sudah makan?")
if makan  == "tidak" :
    total_persiapan_makan= waktu_persiapan_awal + waktu_makan 
    print (f"kamu harus makan dalam waktu {total_persiapan_makan}")
else:
    print(f"lanjut mandi")

# mandi
mandi = input ("Apakah kamu sudah mandi?")
if mandi == "tidak":
    total_persiapan_mandi= waktu_persiapan_awal + waktu_mandi
    print (f"kamu harus mandi dalam waktu {total_persiapan_mandi}")
else :
    print (f"lanjut pilih kendaraan")
    

kendaraan = input ("pilih pakai motor atau jalan kaki?")
if kendaraan == "motor" :
    waktu_berangkat = waktu_persiapan_awal + total_persiapan_makan + total_persiapan_mandi + waktu_pakaimotor
    print (f"waktu yang diperlukan adalah {waktu_berangkat} menit")
if kendaraan == "jalan kaki":
    waktu_berangkat_jalan = waktu_persiapan_awal + total_persiapan_makan + total_persiapan_mandi + waktu_jalankaki
    

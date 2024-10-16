waktu_makan= 15 
waktu_mandi= 10
jalan_kaki= 30
motor = 10
makan = input("sudah makan?:")
mandi = input ("sudah mandi?:")
tranportasi = input ("pilih tranportasi:")
total_waktu_persiapan = waktu_makan+waktu_mandi+motor
if makan == "tidak" and mandi == "tidak" or tranportasi == "motor":
    print(f"total waktu persiapan anda {total_waktu_persiapan}")


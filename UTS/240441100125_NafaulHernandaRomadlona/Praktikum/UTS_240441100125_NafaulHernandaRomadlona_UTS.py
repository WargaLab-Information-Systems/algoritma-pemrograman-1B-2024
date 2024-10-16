"Semangat ngampus"


# waktu persiapan
makan = str(input("kamu udah makan atau belum? (sudah/belum)"))
belum_makan = 0

if makan == "belum":
    print("Jika belum makan, kamu perlu mengalokasikan waktu 15 menit untuk makan.")
    belum_makan = 15
else :
    print("Kamu bisa langsung lanjut ke tahap berikutnya jika sudah makan.")

mandi = str(input("Kamu sudah mandi atau belum? (sudah/belum)"))
belum_mandi = 0 
if mandi == "belum" :
    print("Jika belum mandi, kamu perlu mengalokasikan waktu 10 menit untuk mandi.")
    belum_mandi = 10    
else :
    print("Jika sudah mandi, lanjutkan ke tahap berikutnya.")
waktu_persiapan = belum_makan + belum_mandi

transportasi=str(input("Pilih transportasi : (jalan kaki/motor)"))
waktu_perjalanan = 0
if transportasi == "jalan kaki" or "motor" :
    if transportasi == "jalan kaki" :
        waktu_perjalanan= 30
    if transportasi == "motor" :
        waktu_perjalanan =15
total_waktu= waktu_perjalanan + waktu_persiapan
maksimal_waktu = 50
print("total waktu yang dibutuhkan kamu berangkat adalah",total_waktu,"menit")
if total_waktu > maksimal_waktu :
    print("kamu akan terlambat")




 



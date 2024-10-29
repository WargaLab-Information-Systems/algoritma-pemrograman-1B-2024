# deklarasi variabel untuk menyimpan waktu 
waktu_persiapan = 0 

# menanyakan status makan
status_makan = input("apakah kamu sudah makan (y/n) = ")
if(status_makan == "n"):
    waktu_persiapan +=15

#menanyakan status mandi
pilihan_transportasi = input("apakah kamu berjalan kaki atau menggunakan motor? ")
while True:
    if(pilihan_transportasi == "motor"):
        waktu_transportasi = 15
        break
    elif(pilihan_transportasi == "jalan"):
        waktu_transportasi = 30
        break
    else:
        print("input kamu salah! ulangi lagi")
        pilihan_transportasi = input("apakah kamu berjalan atau menggunakan motor? ")

# total waktu persiapan
total_waktu = waktu_persiapan + waktu_transportasi

#status terlambat
if(total_waktu >= 50):
    print(f"waktu persiapan anda {total_waktu}")
    print("kamu tepat waktu")
else:
    print(f"waktu persiapan anda {total_waktu}")
    print("kamu terlambat")

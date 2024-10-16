
makan = 15
mandi = 10
jalan = 30
motor = 15
waktu = ""
sisa = ""
w_terlambat = ""
terlambat = 60
y = 'y'
input ("apakah kamu sudah makan : ")
if  y  :
    print("saya sudah makan")
else  :
    waktu += makan
    print("saya akan makan terlebih dahulu")

input ("apakah kamu sudah mandi : ")
if y :
    print("saya sudah mandi")
else :
    waktu += mandi
    print("saya akan pergi mandi terlebih dahulu")

input ("transportasi apa yang aka kamu pilih : ")
if y :
    print("saya akan pergi ke kampus")
    if jalan :
     waktu += jalan 
    print(f"Saya akan jala kaki yang akan membutuhkan waktu {jalan} menit ke kampus ")
    if motor :
     waktu += motor 
    print(f"Saya akan menggunakan Motor yang akan membutuhkan waktu selama {motor} menit ke kampus ")
else : 
    print("saya malas jalan kaki  dan saya tidak memiliki kendaraan bermotor")

if waktu < terlambat :
   terlambat - waktu == sisa
   print (f"saya tidak terlambat masih memiliki waktu tersisa {sisa} menit")
else :
   waktu - terlambat == w_terlambat
   print(f"saya terlambat pergi ke kampus selama {w_terlambat}")
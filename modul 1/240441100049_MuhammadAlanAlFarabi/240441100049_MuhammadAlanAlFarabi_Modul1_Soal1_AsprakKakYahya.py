# soal 1
print("jawaban no 1")
print("memcari volume")
# Celengan berbentuk balok mempunyai panjang 20 cm, lebar 13 cm dan tinggi 7 cm
# rumusnya adalah panjang*lebar*tinggi

panjangB = 20
lebarB   = 13
tinggiB  = 7

volumeB  = panjangB*lebarB*tinggiB
print("Volume dari balok adalah ", volumeB, "cm3")

# celengan berbentuk tabung memiliki diameter 14 cm dan luas selimut 440 Cm2
# rumusnya adalah phi*jari jari*jari jari*tinggi
# jari jari adalah diameter di bagi 2
# karena tinggi belum di ketahui, kita cari dulu, rumusnya adalah luas/2*22/7*jari jari

diameterT  = 14
luas_ST    = 440

jariT      = diameterT/2
tinggiT    = (luas_ST/2)/(22/7*jariT)

volumeT    = 22/7*jariT*jariT*tinggiT

print("volumenya dari tabung adalah ", volumeT, "cm3")
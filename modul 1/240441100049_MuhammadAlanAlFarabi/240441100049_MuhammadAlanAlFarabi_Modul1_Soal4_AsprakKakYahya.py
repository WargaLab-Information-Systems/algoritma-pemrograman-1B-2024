# soal
print("soal no 4")
print("berapa cara yang dapat digunakan untuk memilih tim")
# 7 orang dan hanya 4 yang dipilih, berapa metode yang dapat digunakan

orang = 7
n     = 5040 # n adalah faktorial dari nilai orang
pilih = 4
r     = 24 # r adalah faktorial dari orang yang bisa di pilih
nCr   = 6 # nCr adalah hasil dari (n-r)! 7 - 4 kemudian di faktorisasikan.

rumusP  = (n)//(r*nCr)
print("jadi cara yang bisa di gunakan oleh darsono ada ", rumusP, "cara")
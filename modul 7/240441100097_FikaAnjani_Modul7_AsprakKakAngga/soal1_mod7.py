peminjaman ={
    "alat pengukur tekanan darah" : 0,
    "termometer" : 0,
    "stetoskop" : 0,
    "inhaler" : 0
}

print("=======Proses Peminjaman dan Pengembalian Alat Kesehatan=======")
print("hari pertama :")
peminjaman["alat pengukur tekanan darah"] += int(input("berapa alat pengukur tekanan darah yang di pinjam? :"))
peminjaman["termometer"] += int(input("berapa termometer yang dipinjam? :"))
print ("barang yang di pinjam pada hari pertama")
print(peminjaman)

print("hari kedua :")
peminjaman["stetoskop"] += int(input("berapa stetoskop yang di pinjam? :"))
print("barang yang di pinjam pada hari kedua")
print (peminjaman)

print("seminggu kemudian :")
peminjaman["alat pengukur tekanan darah"] -= int(input("berapa alat pengukur tekanan darah yang di kembalikan? :"))
peminjaman["termometer"] -= int(input("berapa termometer yang di kembalikan? :"))
peminjaman["stetoskop"] -= int(input("berapa stetoskop yang akan di tukar? :"))
peminjaman["inhaler"] += int(input("berapa inhaler yang dipinjam? :"))
print("barang yang di pinjam setelah seminggu")
print(peminjaman)


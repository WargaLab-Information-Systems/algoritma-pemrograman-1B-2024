#nim wuland 150451100006
nama = input("Masukkan nama :")
nim = int(input("Masukkan nim kamu :"))
NilaiUts = float(input("Masukkan nilai UTS kamu :"))
NilaiUas = float(input("Masukkan nilai UAS kamu :"))

rata = (NilaiUts + NilaiUas) / 2

if rata >= 81:
    status = "Anda mendapatkan nilai A"
elif rata >= 71:
    status = "Anda mendapatkan nilai B"
elif rata >= 61:
    status = "Anda mendapatkan nilai C"
elif rata >= 41:
    status = "Anda mendapatkan nilai D"
else:
    status = "Anda mendapatkan nilai E"

print("Nama anda " + nama)
print("Nim anda", nim)
print("Nilai rata rata anda adalah", rata )
print(status)
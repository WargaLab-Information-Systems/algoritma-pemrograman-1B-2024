nama = str(input("Masukan nama anda= "))
nim = str(input("Masukan nim anda= "))

uts = int(input("Masukan nilai UTS anda= "))
uas = int(input("Masukan nilai UAS anda= "))

r = (uts + uas) / 2

if r >=81 and r <= 100:
    print(nama)
    print(nim)
    print("nilai anda adalah", r, "A")
elif r >=71 and r <= 80:
    print(nama)
    print(nim)
    print("nilai anda adalah", r, "B")
elif r >=61 and r <= 70:
    print(nama)
    print(nim)
    print("nilai anda adalah", r, "C")
elif r >=41 and r <= 60:
    print(nama)
    print(nim)
    print("nilai anda adalah", r, "D")
elif r >=0 and r <= 40:
    print(nama)
    print(nim)
    print("nilai anda adalah", r, "E")
else:
    print(nama)
    print(nim)
    print("nilai anda adalah", r, "Tidak Valid")
nama = str(input("Masukan nama anda= "))
nim = str(input("Masukan nim anda= "))

uts = int(input("Masukan nilai UTS anda= "))
uas = int(input("Masukan nilai UAS anda= "))

r = (uts + uas) / 2

if r >=81:
    print(nama)
    print(nim)
    print("nilai anda adalah", r, "A")
else:
    if r >71:
        print(nama)
        print(nim)
        print("nilai anda adalah", r, "B")
    else:
        if r >=61:
            print(nama)
            print(nim)
            print("nilai anda adalah", r, "c")
        else:
            if r >=41:
                print(nama)
                print(nim)
                print("nilai anda adalah", r, "D")
            else:
                print(nama)
                print(nim)
                print("nilai anda adalah", r, "E")

        
 















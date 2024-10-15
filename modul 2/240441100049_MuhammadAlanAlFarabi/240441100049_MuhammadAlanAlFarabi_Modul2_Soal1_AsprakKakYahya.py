nama    = str(input("Masukan Nama anda: "))
nim     = str(input("Masukan Nim anda: "))
# inputan data string, nama dan nim

uts = int(input("Masukan Nilai UTS anda: "))
uas = int(input("Masukan Nilai UAS anda: "))
# inputan data integer, nilai uts dan uas

r = (uts + uas) / 2
# rumus rata - rata adalah jumlah nilai di bagi jumlah data.

if  r >=81 and r <=100:
    print("Nama anda adalah", nama)
    print("Nim anda adalah", nim)
    print("nilai rata rata kamu adalah", r,  " A")
else:
    if r >= 71 and r <=80:
        print("Nama anda adalah", nama)
        print("Nim anda adalah", nim)
        print("nilai rata rata kamu adalah", r,  " B")
    else:
        if r >= 61 and r <=70:
            print("Nama anda adalah", nama)
            print("Nim anda adalah", nim)
            print("nilai rata rata kamu adalah", r,  " C")
        else:
            if r >= 41 and r <=60:
                print("Nama anda adalah", nama)
                print("Nim anda adalah", nim)
                print("nilai rata rata kamu adalah", r,  " D")
            else:
                if r >= 0 and r <=40:
                    print("Nama anda adalah", nama)
                    print("Nim anda adalah", nim)
                    print("nilai rata rata kamu adalah", r,  " E")
                else:
                    print("Nama anda adalah", nama)
                    print("Nim anda adalah", nim)
                    print("nilai rata rata anda diluar ketentuan")

# Penyeleksi kondisi
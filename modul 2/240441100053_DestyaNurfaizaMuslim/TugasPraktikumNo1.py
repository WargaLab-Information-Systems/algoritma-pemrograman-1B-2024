# Penyeleksian kondisi secara dinamis

nama = input("Masukkan nama anda : ")
nim = input("Masukkan NIM anda : ")
uts = int(input("Maukkan nilai UTS : "))
uas = int(input("Masukkan nilai UAS : "))

print("Nama anda adalah ", nama)
print("NIM anda adalah ", nim)

rata_rata = (uts + uas) / 2
print("Nilai rata-rata nilai anda ", rata_rata)

if rata_rata >=81 and  rata_rata <=100:
    print("Anda mendapatkan nilai A")
elif rata_rata >=71 and  rata_rata <=80:
    print("Anda mendapatkan nilai B")
elif rata_rata >=61  and  rata_rata <=70:
    print("Anda mendapatkan nilai C")
elif rata_rata >=41  and  rata_rata <=60:
    print("Anda mendapatkan nilai D")
elif rata_rata >=0  and  rata_rata <=40:
    print("Anda mendapatkan nilai E")
else :
    print("Nilai yang anda masukkan salah")
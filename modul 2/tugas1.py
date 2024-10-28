nama = (input("Masukkan nama anda : "))
NIM = (input("Masukkan NIM anda : "))
nilai_uts = int(input("Masukkan nilai UTS anda : "))
nilai_uas = int(input("Masukkan nilai UAS anda : "))

print(f"Nama anda adalah {nama}")
print(f"NIM anda : {NIM}")

ratarata = (nilai_uts + nilai_uas) / 2
print(f"Nilai rata rata anda adalah {ratarata} ")

if ratarata >=81 and ratarata<=100:
    print("Anda mendapatkkan nilai A")
elif  ratarata >=71 and ratarata <=80:
    print("Anda mendapatkkan nilai B")
elif ratarata >=61 and ratarata <=70:
    print("Anda mendapatkkan nilai C")
elif ratarata >=41 and ratarata <=60:
    print("Anda mendaptakkan nilai D")
else:
    print("Anda mendapatkkan nilai E")
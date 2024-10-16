#data
nama = (input("Masukan nama anda"))
nim = (input("Masukan Nim anda"))
nilai_uts = int(input("Masukan nilai UTS anda"))
nilai_uas = int(input("Masukan nilai UAS anda"))

#Menghitung rata-rata 
rata_rata = (nilai_uas + nilai_uts) / 2

print(f"Masukan Nama anda: ", nama)
print(f"Masukan Nim anda: ", nim)
print(f"Nilai rata-rata anda ", rata_rata)

if rata_rata>= 81  and rata_rata <=100:
    print("Anda mendapatkan nilai A")
elif rata_rata>=71 and rata_rata <=80:
    print("Anda mendapatkan nilai B")
elif rata_rata>=61 and rata_rata  <=70:
    print("Anda mendapatkan nilai C")
elif rata_rata>=41 and rata_rata <=60:
    print("Anda mendapatkan nilai D") 
else: 
    print("Anda mendapatkan nilai E")
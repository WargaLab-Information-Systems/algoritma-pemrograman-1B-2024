nama = (input("MASUKKAN NAMA ANDA: "))
nim = int(input("MASUKKAN NIM ANDA: "))
nilai_uts = int(input("MASUKKAN NILAI UTS ANDA: "))
nilai_uas = int(input("MASUKKAN NILAI UAS ANDA: "))

nilai_rara_rata = (nilai_uts + nilai_uas)/2
print("NILAI RATA RATA ANDA ADALAH", nilai_rara_rata)

# NILAI RATA RATA
a = int(input("\nMASUKKAN NILAI RATA RATA ANDA: "))

if a >= 81 <= 90 :
    print("ANDA MENDAPATKAN NILAI A")
elif a >= 71 <= 80 :
    print("ANDA MENDAPATKAN NILAI B")
elif a >= 61 <= 70 :
    print("ANDA MENDAPATKAN NILAI C")
elif a >= 41 <= 60 :
    print("ANDA MENDAPATKAN NILAI D")
else : 
    print("ANDA MENDAPATKAN NILAI E")
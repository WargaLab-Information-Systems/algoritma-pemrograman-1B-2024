Nama = str(input("Masukkan Nama : "))
Nim = int (input("Masukkan Nim : "))
Nilai_UTS = int (input("Masukkan Nilai UTS : "))
Nilai_UAS = int(input("Masukkan Nilai UAS : "))

print(f"Mahasiswa dengan Nama : {Nama}")
print (f"Dengan Nim : {Nim} ")

Nilai_rata_rata = int((Nilai_UTS + Nilai_UAS)/(2))
print("Nilai Rata Rata Anda Adalah", Nilai_rata_rata)

if Nilai_rata_rata >=81 <=100 :
    print ("Anda Mendapatkan Nilai A")
elif Nilai_rata_rata >=71 <=80 :
    print("Anda Mendapatkan Nilai B")
elif Nilai_rata_rata >=61 <=70 :
    print("Anda Mendapatkan Nilai C")
elif Nilai_rata_rata >=51 <=60 :
    print("Anda Mendapatkan Nilai D")
else :
    print("Anda Mendapatkan Nilai E ")
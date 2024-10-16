Nama = (input("Nama :"))
NIM = (input("NIM :"))
nilai_UTS = int(input("Masukkan nilai UTS :"))
nilai_UAS = int(input("Masukkan nilai UAS :"))

nilai_rata_rata = (nilai_UTS + nilai_UAS)/2
if nilai_rata_rata >=81 <=100 :
    print(Nama)
    print(NIM)
    print(nilai_rata_rata)
    print("Anda mendapat nilai A")
    print("Lulus")
elif nilai_rata_rata >=71 <=80 :
    print(Nama)
    print(NIM)
    print(nilai_rata_rata)
    print("Anda mendapat nilai B")
    print("Lulus")
elif nilai_rata_rata >=61 <=70 :
    print(Nama)
    print(NIM)
    print(nilai_rata_rata)
    print("Anda mendapat nilai C")
    print("Lulus bersyarat")
elif nilai_rata_rata >=41 <=60 :
    print(Nama)
    print(NIM)
    print(nilai_rata_rata)
    print("Anda mendapat nilai D")
    print("Maaf anda tidak lulus")
else:
    print(nilai_rata_rata)
    print("Anda tidak lulus")
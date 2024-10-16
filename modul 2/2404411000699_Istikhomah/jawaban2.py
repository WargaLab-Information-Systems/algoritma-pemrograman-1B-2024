# memasukkan variabel dengan input
nama = (input("Masukkan nama Anda "))
skor = int(input("Masukkan skor Anda: "))
IPK = float(input("Masukkan IPK Anda: "))

# seleksi kondisi
if skor > 1100:
    if IPK >= 3.0:
        print("Anda dinyatakan lulus persyaratan beasiswa")
else:
    print("Anda dinyatakan tidak lulus persyaratan beasiswa")

   
        
   
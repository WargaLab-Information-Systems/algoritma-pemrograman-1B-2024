nama = str(input("Masukkan Nama : "))
skor = float(input("Masukkan Skor : "))
ipk = float(input("Masukkan IPK : "))

if skor > 1100 and ipk >= 3.0:
    print("Selamat saudara", nama, "Anda Lulus Persyaratan Beasiswa, Karena Skor anda", skor, "Dan IPK Anda", ipk)
else:
    print("Maaf saudara", nama, "Anda Tidak Lulus Persyaratan Beasiswa, Karena Skor anda", skor, "Dan IPK Anda", ipk)
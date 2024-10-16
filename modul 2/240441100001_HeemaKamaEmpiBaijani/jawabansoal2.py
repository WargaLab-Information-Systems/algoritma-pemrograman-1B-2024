nama = str(input("Masukan Nama : "))
skor = float(input("Masukan Skor : "))
ipk = float(input("Masukan IPK : "))

# a jika ditentukan skor yang lebih besar dari 1100 dan ipk minimal 3.0 untuk lulus persyaratan.

if skor > 1100 and ipk >= 3.0:
    print(f"{nama} dinyatakan Lulus")
else:
    print(f"{nama} dinyatakan Tidak Lulus")
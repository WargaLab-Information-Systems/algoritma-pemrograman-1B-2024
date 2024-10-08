#PENYELEKSIAN KONDISI SECARA DINAMIS

nama = str(input("masukkan nama: "))
NIM = int(input("masukkan NIM: "))
nilai_UTS = int(input("masukkan nilai UTS: "))
nilai_UAS = int(input("masukkan nilai UAS: "))

#rata-rata nilai
rata_rata_nilai =float(nilai_UTS + nilai_UAS) / 2

if rata_rata_nilai >=81 <=100:
    predikat = ("A")
elif rata_rata_nilai >=71 <=80:
    predikat = ("B")
elif rata_rata_nilai >=61 <=70:
    predikat = ("C")
elif rata_rata_nilai >=41 >=60:
    predikat = ("D")
elif rata_rata_nilai >=0 <=40:
    predikat = ("E")
else:
    predikat = ("Nilai anda tidak valid.")
    
print(f"nama mahasiswa:{nama}")
print(f"NIM anda:{NIM}")
print(f"nilai rata-rata anda: {rata_rata_nilai}")
print(f"anda mendapat nilai {predikat}")

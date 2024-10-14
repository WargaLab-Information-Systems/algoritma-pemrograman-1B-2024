# Data Mahasiswa SI
skor_jaka = 1100
ipk_jaka = 3.5

skor_ida = 1000
ipk_ida = 3.5

# Syarat lulus Beasiswa
skor_beasiswa = 1100
ipk = 3.0

# menyeleksi jaka

if skor_jaka >= skor_beasiswa and ipk_jaka >= ipk:
    print("JAKA DINYATAKAN LULUS MENDAPATKAN BEASISWA")
else:
    print("JAKA DINYATAKAN TIDAK LULUS MENDAPATKAN BEASISWA")

# menyeleksi ida

if skor_ida >= skor_beasiswa and ipk_ida >= ipk:
    print("IDA DINYATAKAN LULUS MENDAPATKAN BEASISWA")
else:
    print("IDA DINYATAKAN TIDAK LULUS MENDAPATKAN BEASISWA")
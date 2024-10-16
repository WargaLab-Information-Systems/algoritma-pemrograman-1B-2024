# Mengetahui pernyataan lulus beasiswa
# Dengan syarat skor lebih dari 1100 dan ipk minimal 3.0

skor_jaka = 1100
skor_ida = 1000
ipk_jaka = 3.5
ipk_ida = 3.5

if skor_jaka >= 1100:
    if ipk_jaka > 3.0:
        print("Selamat Jaka, anda diterima")
    else :
        print("Maaf Jaka, anda tidak diterima karena ipk tidak memenuhi syarat")
else:
    print("Maaf Jaka, anda tidak diterima karena skor tidak memenuhi syarat")

if skor_ida >= 1100:
    if ipk_ida > 3.0:
        print("Selamat Ida, anda diterima")
    else :
        print("Maaf Ida, anda tidak diterima karena ipk tidak memenuhi syarat")
else:
    print("Maaf Ida, anda tidak diterima karena skor tidak memenuhi syarat")




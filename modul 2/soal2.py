skor_jaka = 1100
ipk_jaka = 3.5
skor_ida = 1000
ipk_ida = 3.5

if skor_jaka > 1100 and ipk_jaka >= 3.0:
    print("jaka dinyatakan lolos untuk menjadi penerima beasiswa dikarenakan skor dan ipk yang sesuai dengan persyaratan")
elif skor_ida > 1100 and ipk_ida >= 3.0:
    print("ida dinyatakan lolos untuk menjadi penerima beasiswa dikarenakan skor dan ipk yang sesuai dengan persyaratan")
else:
    print("tidak ada yang memenuhi untuk menjadi penerima beasiswa dikarenakan skor dan ipk yang tidak sesuai dengan persyaratan")

skor_jaka = 1100
ipk_jaka = 3.5

skor_ida = 1000
ipk_ida = 3.5

skor_min = 1100
ipk_min = 3.0

if skor_jaka >= skor_min and ipk_jaka >= ipk_min:
    print("Jaka lulus persyaratan beasiswa.")
else:
    print("Jaka tidak lulus persyaratan beasiswa.")

if skor_ida > skor_min and ipk_ida >= ipk_min:
    print("Ida lulus persyaratan beasiswa.")
else:
    print("Ida tidak lulus persyaratan beasiswa.")

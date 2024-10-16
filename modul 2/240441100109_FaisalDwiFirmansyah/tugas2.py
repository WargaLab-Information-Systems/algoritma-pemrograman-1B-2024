skor_jaka = 1100
ipk_jaka = 3,5

skor_ida = 1000
ipk_ida = 3,5

min_skor = 1100
min_ipk = 3,0

if skor_jaka >= min_skor and ipk_jaka > min_ipk:
    print("Jaka lulus persyaratan beasiswa")
else:
    print("Jaka tidak lulus persyaratan beasiswa")

if skor_ida >= min_skor and ipk_ida > min_ipk:
    print("Ida lulus persyaratan beasiswa")
else:
    print("Ida tidak lulus persyaratan beasiswa")
skor_jaka=1100
ipk_jaka=3.5

skor_ida=1000
ipk_ida=3.5

skor_lulus=1100
ipk_lulus=3.0

if (skor_jaka >= skor_lulus) and (ipk_jaka >= ipk_lulus):
    print("jaka lulus persyaratan beasiswa")
else:
    print("jaka tidak lulus persyaratan beasiswa")

if (skor_ida >= skor_lulus) and (ipk_ida >= ipk_lulus):
    print("ida lulus persyaratan beasiswa")
else:
    print("ida tidak lulus persyaratan beasiswa")
skor_jaka = 1100
ipk_jaka = 3.5
skor_ida = 1000
ipk_ida = 3.5

minimal_skor = 1100
minimal_ipk = 3.0

#JAKA
if skor_jaka > minimal_skor and ipk_jaka > minimal_ipk:
    print("Jaka lulus persyaratan beasiswa")
else:
    print("Jaka tidak lulus persyaratan beasiswa")
    
#IDA
if skor_ida > minimal_skor and ipk_ida > minimal_ipk:
    print("Ida lulus persyaratan beasiswa")
else:
    print("Ida tidak lulus persyaratan beasiswa")
    
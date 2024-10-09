#data
skor_jaka = 1100
skor_ida = 1000 
ipk_jaka = 3.5
ipk_ida = 3.0
#persyaratan 
minimal_skor = 1100
minimal_ipk = 3.5

#jaka
if skor_jaka >= minimal_skor and ipk_jaka >= minimal_ipk :
    hasil_jaka = "Jaka lulus persyaratan beasiswa"
else: 
    hasil_jaka = "Jaka tidak lulus ppersyaratan beasiswa"

#ida
if skor_ida >= minimal_skor and ipk_ida>= minimal_ipk :
    hasil_ida = "Ida lulus persyaratan beasiswa"
else: 
    hasil_ida = "Ida tidak lulus persyaratan beasiswa"

#manggil siapa yg lulus
print(hasil_jaka)
print(hasil_ida)
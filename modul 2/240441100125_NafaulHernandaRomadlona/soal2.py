q = 1100
p = 1000
r = 3,5
s = 3,0
min_ipk =3,0
min_skor=1100
jaka = q and r
ida = p and s
syarat_lulus_beasiswa=min_ipk and min_skor
if q > min_skor and r >= min_ipk :
    print("Jaka lulus beasiswa")
else :
    print("jaka tidak lulus beasiswa")
if p > min_skor and s >= min_ipk :
    print("ida lulus beasiswa")
else :
    print("ida tidak lulus beasiswa")
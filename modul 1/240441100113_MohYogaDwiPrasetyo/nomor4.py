jumlh_org = 7
jumlh_terpilih = 4
beda = jumlh_org - jumlh_terpilih # 3

faktorial_jumlh_org = 7*6*5*4*3*2*1 # 5040
faktorial_jumlh_terpilih = 4*3*2*1 # 24  
faktorial_beda = 3*2*1 # 6

kombinasi = faktorial_jumlh_org / (faktorial_jumlh_terpilih * faktorial_beda) 
print(f"Jumlah cara membentuk tim {jumlh_org} orang dari {jumlh_terpilih} orang adalah: {kombinasi} cara")
# diket

jumlah_orang = 7
jumlah_dipilih = 4
faktorial_1 = 1 
faktorial_2 = 1
faktorial_3 = 1
#rumus kombinasi = n!/r!*(n-r)! jumlah_orang!/jumlah_dipilih!*(jumlah_orang-jumlah_dipilih)!

for i in range (1, jumlah_orang+1):
    faktorial_1 *= i 
# faktorial_1 = faktorial_1*i
# faktorial_1 = faktorial_1*1 (1*1)(1)
# faktorial_1 = faktorial_1*2 (1*2)(2)
# faktorial_1 = faktorial_1*3 (2*3)(6)
# faktorial_1 = faktorial_1*4 (6*4)(24)
# faktorial_1 = faktorial_1*5 (24*5)(120)
# faktorial_1 = faktorial_1*6 (120*6)(720)
# faktorial_1 = faktorial_1*7 (720*7)(5040)

for i in range (1, jumlah_dipilih+1):
    faktorial_2 *= i
# faktorial_2 = faktorial_2*i
# faktorial_2 = faktorial_2*1 (1*1)(1)
# faktorial_2 = faktorial_2*2 (1*2)(2)
# faktorial_2 = faktorial_2*3 (2*3)(6)
# faktorial_2 = faktorial_2*4 (6*4)(24)

for i in range (1, (jumlah_orang-jumlah_dipilih)+1): 
    faktorial_3 *= i
# faktorial_3 = faktorial_3*i
# faktorial_3 = faktorial_3*1 (1*1)(1)
# faktorial_3 = faktorial_3*2 (1*2)(2)
# faktorial_3 = faktorial_3*3 (2*3)(6)

hasil_kombinasi = faktorial_1 / (faktorial_2 * faktorial_3)
print("jumlah n! : ", faktorial_1)
print("jumlah r! : ", faktorial_2)
print("jumlah (n-r)! : ", faktorial_3)
print("jumlah banyak cara : ", hasil_kombinasi)
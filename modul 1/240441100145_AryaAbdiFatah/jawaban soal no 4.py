print("tugas nomor 4")

# Darsono memiliki total 7 orang ingin memilih 4 orang untuk dijadikan satu regu
# C(7,4) = 7! / 4! ( 7 - 4)!
#        = 7! / 4! * 3!
# ini saya kurangkan dari 7! dengan 4!
faktorial7 = 7*6*5
faktorial3 = 3*2

hasil = faktorial7 / faktorial3
print("jadi, Darsono ada", hasil ,"cara untuk memilih 4 orang dari 7 orang untuk masuk kedalam tim nya")

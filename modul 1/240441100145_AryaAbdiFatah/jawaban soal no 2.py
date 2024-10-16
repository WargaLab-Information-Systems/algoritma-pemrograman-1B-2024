print ("soal nomor 2")

# tugas nomor 2
# ditanya jumlah 8 suku pertama
# diketahui persamaan 1: suku ke 5 = 11
# diketahui persamaan 2: jumlah suku ke 8 dan suku ke 12 = 52
# persamaan 1 = a + 4b =11
# persamaan 2 = (a + 7b) + (a + 11b) = 52
# dari persamaan ke 1 kita bisa mendapatkan nilai a dari a = 11 - 4b
# dengan menemukan nilai a kita bisa subtitusikan di persamaan 2
# (11 - 4b + 7b) + (11 - 4b + 11b) = 52
# =  11 + 3b + 11 + 7b = 52
# = 10b + 22 = 52
# = 10b = 52 - 22
# = 10b = 30
# = b = 3

b = 3 
a = 11 - 4 * b # a = 11 - 4 * 3 a = 11 -12 = -1
n = 8 

jumlahsukupertama = (n / 2)*(2 * a + (n - 1 )* b) # Un = a + (n - 1)*b #Sn = n/2 (a+Un) 
print("jumlah nilai dari 8 suku pertama adalah" , jumlahsukupertama)
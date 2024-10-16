suku_5 = 11
suku_12_8 = 52

# persamaan dihitung manual 
# persamaan 1 --> 11 = a + 4b
# persamaan 2 --> 52 = a + 7b + a + 11b. 52 = 2a + 18b 
# eliminasi (b) 26 = a + 9b - 11 = q + 4b = 15 = 5b. b= 3
# eliminasi (a) 11 = a + 4.3, 11 = a + 12. a = -1

b = 3 #selisih antar suku
a = suku_5 - (5-1)*b # suku awal 

#rumus 5n = (n/2)*(2a+(n-1)b)
n = 8
sn = (n/2)*(2*a+(n-1)*b)

print(f"jumlah 8 suku pertama adalah {sn}")
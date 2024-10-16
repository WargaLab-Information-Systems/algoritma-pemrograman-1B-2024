#VARIABEL
nama = "heema"
umur = 17
tinggi_badan = 178.9
#print("nama saya {nama}, umur saya str{umur}, tinggi badan saya {tinggi_badan} cm")
print("nama saya" + nama + ", umur saya" + str(umur) + ",tinggi" + str (tinggi_badan))

#OPERASI ARITMATIKA
a= 12
b = 5

penjumlahan = a + b
pengurangan = a - b
perkalian = a * b
pembagian = a / b
pangkat =  a ** b
modulus = a % b
bilangan_bulat = a // b

print(penjumlahan)
print(pengurangan)
print(perkalian)
print(pembagian)
print(pangkat)
print(modulus)
print(bilangan_bulat)

#OPERATOR BOOLEAN 
x = True
y = False

hasil_and = x and y
hasil_or = x or y
hasil_not = not x
print(hasil_not)

#OPERATOR LOGIKA
x = 5

print (x>3 and x<10)

#OPERATOR HIMPUNAN
a = {1, 2, 3}
b = {3, 4, 5}

penggabungan = a | b

#operator tenary 
umur = 18
status = "dewasa" if umur >= 18 else "belum dewasa"
print(status) #output dewasa

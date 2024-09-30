u5=int(input("masukkan nilai dari u5: "))
u8_u12=int(input("masukkan nilai u8_u12: "))

# menghitung beda(b)
b=(u8_u12-2*u5)/ 10

#mencari suku pertama 
a=u5-4*b

#menghitung jumlah 8 suku pertama 
n=8
jumlah_8_suku= n*(2*a+(n-1)*b)/2

#mencari hasil
print(f"jadi hasil suku pertama adalah: ", a)
print(f"Jadi bedanya adalah: ", b)
print(f"Jadi jumlah 8 suku pertama", jumlah_8_suku)
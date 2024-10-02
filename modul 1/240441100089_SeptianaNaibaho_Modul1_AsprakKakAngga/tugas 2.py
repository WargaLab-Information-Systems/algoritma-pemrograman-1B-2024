# u5= 11
# u8ditambahu12= 52

u5= int(input("masukkan u5 :"))
u8ditambahu12= int(input("masukkan u8_ditambah_u12 :"))

# u5 = a + 4*b = 11 #persamaan 1
# u8ditambahu12 = 2*a + 18*b #persamaan 2

# #persamaan 
# a + b = 11
# a = 11- 4*b

# #subsitusikan a ke persamaan 2
# 2*(11 - 4*b) + 18*b = 52
# 22 - 8*b + 18*b = 52
# 22 + 10*b =52
# 10*b = 30
b=3
a = u5 - 4*b
n= 8
sn= n/2*(2*a+(n-1)*b)
s8= 8/2*(2*a+(8-1)*b)
print(f"jumlah 8 suku pertama adalah : {s8}")





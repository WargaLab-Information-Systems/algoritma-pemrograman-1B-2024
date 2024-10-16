# while
x = "AlproB"

while x:
    print(x)
    x = x[1:] # ngurangi satu demi satu huruf nya AlproB

a = 0; b = 10

while a<b:
    print(a)
    a = a+1

# #For
for i in [5,4,3,2,1]:
    print(i)

for i in range (1,10,2):
    print(i)

thnawal = int(input("Masukkan tahun awal: "))
thnakhir = int(input("Masukkan Tahun akhir: "))

for thnawal in range(thnawal, thnakhir):
    if((thnawal % 400 == 0) or (thnawal % 4 == 0) and (thnawal % 100 != 0)):
        print(f"{thnawal} adalah tahun kabisat")
else:
    print(f"{thnakhir} adalah bukan tahun kabisat")

a = 1
for i in range(5):
    if a<=5:
        print("*"*a)
        a +=1

# Break
x = 4
while x < 5:
    if x == 3:
        break
    print(x)
    x = x + 1
else:
    print("loop selesai")

# continue
n = 10
for i in range (1,10):
    if i % 2 == 0:
        continue
    print(i)

# pass
for i in range (5):
    if i == 3:
        pass
    else:
        print(i)



# contoh if
x = 5
if x == 5:
    print("x sama dengan 5")

x = "alprob"
if x == "alprob" :
    print("x sama dengan alprob")
else:
    print("passsword tidak sesuai")
    
nilai = int(input("masukkan nilai anda: "))

if nilai >= 80 <=100:
    print("nilai anda bagus")
elif nilai >= 70 <=79:
    print("boleh juga")
else:
    print("coba lagi")
    
x = 10
if x > 5:
    print("x lebih besar dari 5")

if x < 10:
    print("x lebih kecil dari 15")
    
if x == 10:
    print("x sama dengan 10")

#if bersarang
x = int(input("masukkan nilai x: "))
y= int(input("masukkan nilai y: "))

if x == y:
    print("nilai x sama dengan y")
else:
    if x > y:
        print("nilai x lebih besar dari y")
    elif x < y:
        print("nilai x kurang dari y")
        
#if ternary
nilai = int(input("masukan nilai= "))
print("lulus") if nilai >=75 else print("coba lagi")
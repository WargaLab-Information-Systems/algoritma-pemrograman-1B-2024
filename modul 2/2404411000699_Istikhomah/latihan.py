# contoh if
x = 5
if x == 5:
    print("x sama dengan 5")

x = "alprob"
if x == "alprob" :
    print("x sama dengan alprob")

# contoh kondisi if else
password = "alprob"
if password == "alprob":
    print("password sesuai")
else:
    print("password tidak sesuai")

# contoh if elif else
nilai = int(input("masukkan nilai anda: "))
if nilai >= 80 <= 100:
    print ("nilai anda bagus")
elif nilai >= 70 <= 79:
    print("boleh juga")
elif nilai >=40 <= 50:
    print("remedial dah")
else:
    print("coba lagi")

# contoh if 3x
x = 10

if x > 5:
    print("x lebih besar dari 5")
if x < 10:
    print("x lebih kecil dari 15")
if x == 10:
    print("x sama dengan 10")

# contoh if bersarang
x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))

if x == y:
    print("nilai x sama dengan y")
else:
    if x > y:
        print("nilai x lebih besar dari y")
    elif x < y:
        print("nilai x lebih kecil dari y")

# ternary 
nilai = int(input("masukkan nilai = "))
print("Lulus") if nilai >= 75 else print("Coba lagi")

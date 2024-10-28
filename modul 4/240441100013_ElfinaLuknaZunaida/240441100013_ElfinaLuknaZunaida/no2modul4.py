desimal = int(input("Masukkan bilangan desimal: "))
biner = "" 

while desimal > 0: 
    sisa = desimal % 2 
    biner = str(sisa) + biner  
    desimal = desimal // 2 
print("Hasil konversi ke biner:", biner)


i = 1 
while True: 
    if i <= 0: 
        break

    digit = biner[i - 1:i] 
    if digit == "":  
        break
    print(biner[:1]) 
    i += 1



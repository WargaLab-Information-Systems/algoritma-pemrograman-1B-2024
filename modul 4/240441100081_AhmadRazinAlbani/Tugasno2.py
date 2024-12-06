desimal = int(input("Masukkan bilangan desimal: "))
if desimal == 0:
    biner = "0"
else:
    biner = ""
    n = desimal
    while n > 0:
        sisa = n % 2
        biner = str(sisa) + biner
        n //= 2 

for i in range(1, len(biner)+1):
    print(biner[:i])



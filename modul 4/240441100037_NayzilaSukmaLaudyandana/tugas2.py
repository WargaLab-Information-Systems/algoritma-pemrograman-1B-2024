desimal = int(input("masukkan bilangan desimal: "))

biner = ""
while desimal > 0:
    biner = str(desimal % 2) + biner
    desimal = desimal // 2 
for i in range(1, len(biner) + 1 ):
    print(biner[:i])
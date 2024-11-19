desimal = int(input('masukan bilangan desimal: '))
biner =''

while desimal > 0:
    sisa = desimal%2
    biner = str(sisa)+biner
    desimal = desimal//2

for i in range(1, len(biner)+1):
    print(biner[:i])
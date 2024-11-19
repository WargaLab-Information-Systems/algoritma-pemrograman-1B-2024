desimal = int(input("masukkan bilangan desimal : "))

biner =""
n = desimal
panjang_biner = 0

while n > 0:
    biner = str(n % 2) + biner
    n //= 2
    panjang_biner += 1

print(f"hasil bilangan ke binner : {biner} ")

print("pola segitiga :")
for i in range(1, panjang_biner + 1):
    print(biner[:i])  
angka_desimal = int(input("Masukkan bilangan desimal: "))
bilangan_biner = list()
while angka_desimal != 0:
        rumus_biner = angka_desimal % 2
        bilangan_biner.append(rumus_biner)
        angka_desimal=angka_desimal // 2
print("Pola segitiga dari bilangan biner:")
n = len(bilangan_biner)
for i in range(n):
    for j in range(i + 1):
        print(bilangan_biner[j], end=" ")
    print()
          

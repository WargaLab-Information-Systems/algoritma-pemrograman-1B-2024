print("049")
a = int(input("masukan ukuran angka yang anda inginkan: "))


for i in range(1, a + 1, 1):
    if i == 1:
        print("*" * a)
    if i < a:
        print("*" + " " * (a - 2) + "*")
    if i == a:
        print("*" * a)
# untuk simbol angka 0
for o in range(1, a + 1, 1):
    if o <= a // 2:
        print("*" + " " * (a - 2) + "*")
    if o == a // 2:
        print("*" * a)
    if o >= a // 2:
        print(" " * (a - 1) + "*")
# untuk simbol angka 4

for p in range(1, a + 1, 1):
    if p == 1:
        print("*" * a)
    if p < a // 2:
        print("*" + " " * (a - 2) + "*")
    if p == a // 2:
        print("*" * a)
    if p > (a // 2) + 1:
        print(" " * (a - 1) + "*")
    if p == a:
        print("*" * a)
# untuk simbol angka 9
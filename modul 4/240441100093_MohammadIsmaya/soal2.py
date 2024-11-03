
# Input bilangan desimal dari pengguna
desimal = int(input("Masukkan bilangan desimal: "))

# Mengonversi bilangan desimal ke biner
biner = ""
while desimal > 0:
    sisa = desimal % 2
    biner = str(sisa) + biner
    desimal = desimal // 2

# Menampilkan hasil dalam bentuk pola segitiga
panjang = len(biner) #panjang string biner
for i in range(1, panjang + 1):
    print(biner[:i])


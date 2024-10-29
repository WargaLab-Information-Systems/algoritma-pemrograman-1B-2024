n=int(input("masukkan angka desimal: "))
biner=""
while(n>0):
    biner=str(n%2)+biner
    n=n//2
print(f"Hasil konversi bilangan ke biner adalah {biner}")
print("Pola segitiga: ")
for i in range(len(biner)):
    for j in range(i+1):
        print(biner[j], end=" ")
    print()

tinggi = int(input("Masukkan Tinggi"))

for i in range(tinggi):
    print("  1")
print()

for i in range(tinggi):
    if i == 0 or i == tinggi - 1:  
        print("00000")  
    elif i < tinggi - 1:  
        print("0   0")  
    else:
        print()
print()

for i in range(tinggi):
    print("  1")
print()
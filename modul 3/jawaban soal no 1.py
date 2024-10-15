b = int(input("Masukan ukuran size:"))
#menampilkan angka 1
for o in range (1, b+1, 1):
    if o < b +1:
        print (" " * (b // 2) + "*" + " " * (b // 2))
# menampilkan angka 4
for o in range(1, b+1 ,1):
    if o < b // 2:
        print("*" + " " * (b - 2)+ "*")
    if o == b // 2:
        print("*" * b)
    if o > b // 2:
        print (" " * (b -1) + "*")
#menampilkan angka 5
for o in range (1, b+1, 1):
    if o == 1:
        print ("*" * (b))
    if o < (b // 2)- 1:
        print("*")
    if o == b // 2:
        print("*" * (b))
    if o > (b // 2) + 1:
        print(" " * (b - 1) + "*")
    if o == b:
        print ("*" * (b))





  

  
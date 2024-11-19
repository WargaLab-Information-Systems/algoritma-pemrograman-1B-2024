N = int(input("Masukkan ukuran sisi checkerboard yang diinginkan: "))
karakter = input("pilihlah karakter :(X/O)")
for i in range(0,N+1):
    for j in range(0,N-i):
        print(end=" ")
    for j in range(0,i):
        print(karakter,end=" ")
    print()
if i==N:
    for i in range(N-1,0,-1):
        for j in range(0,N-i):
            print(end=" ")
        for j in range(0,i):
            print(karakter,end=" ")
        print()
N = int(input("Masukkan tinggi:"))
for i in range(N):
    print(""*(N-i) + "*"* (i+1) )
for j in range(N-1):
    print("" *(N+2)+"*" *(N-1-j))
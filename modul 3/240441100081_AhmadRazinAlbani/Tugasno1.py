n = int(input("masukkan size: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 :
            print('*', end='')
        else:
            print('', end=' ')
    print()
print()

for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or j==0 or i==n-1 or j==n-1 :
            print('*', end='')
        else:
            print('', end=' ')
    print()
print()

for i in range(n):
    for j in range(n):
        if j==n//2 :
            print('*', end='')
        else:
            print('', end=' ')
    print()


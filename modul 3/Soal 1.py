size = int(input('masukan size : '))


for i in range(size):
    print("  *  ")

print()

for i in range(size*2):  #Pengulangan from 1 to 7
    for j in range(size):  #Pengulangan from 1 to 7
        if (j == 0 and i <=size-1) or (j == size-1 and i<=size+3) or (i==size-1):
            print("*", end="")
          # Print '+' tanpa baris baru
        else:
            print(" ", end="")  # Print a spase tanpa baris baru
    print()  # pindah line selanjutnya

print()

for i in range(size):
    for j in range(size):
        if i==0 or i==2 or i+j==1+0 or i==size-1 or j==size-1:
            print('h', end='')
        else:
            print('', end=' ')
    print()

n = input('masukan desaing [X/O]: ')
h = int(input('masukan ukuran: '))

if n== 'X' :
    for i in range(h-1):
        for j in range(h-i-1):
            print(' ', end='')
        for j in range(i+1):
            print('X', end=' ')
        print()
    for i in range(h):
        for j in range(i):
            print(' ', end='')
        for j in range(h-i):
            print('X', end=' ')
        print()



if n=='O':
    for i in range(h-1):
        for j in range(h-i-1):
            print(' ', end='')
        for j in range(i+1):
            print('X', end=' ')
        print()
    for i in range(h):
        for j in range(i):
            print(' ', end='')
        for j in range(h-i):
            print('O', end=' ')
        print()
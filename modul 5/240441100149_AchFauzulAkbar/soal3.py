n =int(input('masukan bilangan: '))

def faktorial(n):
    if n==0:
        return 1
    else:
        return n*faktorial(n-1)
print(f'faktorial {n} adalah', faktorial(n))


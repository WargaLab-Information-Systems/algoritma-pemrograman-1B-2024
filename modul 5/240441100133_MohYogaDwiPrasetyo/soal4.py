def cek_palindrom(kata):
    if len(kata) <= 1:
        return True
    
    if kata[0] != kata[-1]:
        return False
    
    return cek_palindrom(kata[1:-1])

kata = input("Masukkan kata: ")    
if cek_palindrom(kata):
    print(f'"{kata}" adalah palindrom')
else:
    print(f'"{kata}" bukan palindrom')
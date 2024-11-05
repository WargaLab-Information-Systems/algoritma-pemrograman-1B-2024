def cek_palindrom(kata):
    #membandingkan kata dengan kebalikan kata
    return kata == kata [::-1]

kata = input(" masukkan kata: ")
if cek_palindrom(kata):
    print(f'"{kata}" adalah palindrom.')
else:
    print(f'"{kata}" bukan palindrom.')
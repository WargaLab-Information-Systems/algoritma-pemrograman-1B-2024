def cek_palindrom(kata):
    kata = kata.replace(" ", "").lower()
    return kata == kata [::-1]

kata = input("Masukkan kata yang akan di cek :")
print(cek_palindrom(kata))

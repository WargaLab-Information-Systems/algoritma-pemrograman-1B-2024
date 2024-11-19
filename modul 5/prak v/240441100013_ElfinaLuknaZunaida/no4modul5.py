def cek_palindrom(kata):
    kata_balikan = kata[::-1]
    return kata == kata_balikan

kata_input = input("Masukkan kata: ")
hasil = cek_palindrom(kata_input)

if hasil:
    print(f"'{kata_input}' adalah palindrom.")
else:
    print(f"'{kata_input}' bukan palindrom.")

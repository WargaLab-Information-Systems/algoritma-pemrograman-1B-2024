def cek_palindrom(kata):
    return kata == kata[::-1]

kata = input("Masukkan kata: ")
palindrom = cek_palindrom(kata)
if palindrom:
    print(f"{kata} adalah palindrom.")
else:
    print(f"{kata} bukan palindrom.")


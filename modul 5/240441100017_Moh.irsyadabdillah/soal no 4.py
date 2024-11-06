def cek_palindrom(kata):
    kata = kata.replace(" ", "").lower()
    
    return kata == kata[::-1]

kata = input("masukkan kata:")

print(f"kata:{kata} adalah palindrom: {cek_palindrom(kata)}")

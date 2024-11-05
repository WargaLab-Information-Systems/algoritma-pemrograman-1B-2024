def cek_palindrom(kata):
    panjang = len(kata)
    for i in range(panjang // 2):
        if kata[i] != kata[panjang - 1 - i]:
            return False
    return True
kata = input("Masukkan sebuah kata: ")
if cek_palindrom(kata):
    print(kata, "Adalah palindrom")
else:
    print(kata, "Bukan palindrom")
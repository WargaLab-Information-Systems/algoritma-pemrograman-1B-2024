def palindrom(kata):
    if kata == kata[::-1]:
        pal = print("Ini kata Palindrom")
        return pal
    else:
        pal = print("Ini Bukan kata Palindrom")
        return pal 


kata = input("Masukkan kata : ")
palindrom(kata)
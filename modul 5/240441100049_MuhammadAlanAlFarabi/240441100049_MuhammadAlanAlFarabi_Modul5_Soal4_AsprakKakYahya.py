def palindrom(kata):
    kata_kecil = ''
    for char in kata:
        if char != ' ':
            kata_kecil += char.lower()

    if kata_kecil == kata_kecil[::-1]:
        return f"{kata} Benar kata palindrom"
    else:
        return f"{kata} Bukan kata palindrom"
    


kata = str(input("Masukan kata yang ingin anda cek: "))
print(f"{kata} adalah ", palindrom(kata))
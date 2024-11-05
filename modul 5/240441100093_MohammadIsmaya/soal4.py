
def cek_palindrom(kata):
    dibalik = ""

    for i in kata:
        dibalik = i + dibalik # Setiap huruf ditambahkan di depan string dibalik
        print(i) 
    
    if dibalik == kata:
        print(f"{dibalik} adalah palindrom")
        return True
    else:
        print(f"{dibalik} adalah bukan palindrom")
        return False

kata = input("Masukkan kata untuk cek palindrom: ")
print(cek_palindrom(kata))
def cek_palindrom():
    kata = input("Masukkan sebuah kata: ")
    kata = kata.lower()

    kata_terbalik = ""
    for i in kata:
        kata_terbalik = i + kata_terbalik
    
    if kata == kata_terbalik:
        print(f"Kata {kata} adalah palindrom.")  
        return True
    else:
        print(f"Kata {kata} bukan palindrom.")  
        return False
cek_palindrom()
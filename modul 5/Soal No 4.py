def cek_palindrom(kata):
    if kata == kata[::-1]: # untuk melangkah mundur satu karakter pada satu waktu,jika tidak pakai - urutanya tidak terbalik
        return f"'{kata}' adalah palindrom"
    else:
        return f"'{kata}' bukan palindrom"

# Contoh penggunaan
print(cek_palindrom("katak"))  
print(cek_palindrom("madam"))  
print(cek_palindrom("hello")) 
print(cek_palindrom("kuda"))
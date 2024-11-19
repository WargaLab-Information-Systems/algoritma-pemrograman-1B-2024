def cek_palindrom(kata):
    # Menghapus spasi dan mengubah huruf menjadi kecil untuk membandingkan
    kata = kata.replace(" ", "").lower()
    # Membandingkan kata dengan kebalikannya
    return kata == kata[::-1]

print(cek_palindrom("katak"))  # Output: True
print(cek_palindrom("madam"))  # Output: True
print(cek_palindrom("hello"))  # Output: False
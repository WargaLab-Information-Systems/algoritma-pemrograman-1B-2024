def cek_palindrom(kata):
    kata = kata
    # Membandingkan kata dengan kebalikannya
    print(kata[::-1])
    return kata == kata[::-1]
    

# Menerima input dari pengguna
kata_input = input("Masukkan sebuah kata: ")
if cek_palindrom(kata_input):
    print(f"{kata_input} adalah palindrom.")
else:
    print(f"{kata_input} bukan palindrom.")
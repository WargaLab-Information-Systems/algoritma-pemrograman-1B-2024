# Kata Palindrom

def cek_palindrom(n):
    balik = n [::-1]
    if (n == balik):
        return True
    else:
        return False

n = input("Masukkan sebuah kata : ")
print("cek_palindrom(n)")
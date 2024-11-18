def cek_palindrom(kata):
    for i in range(len(kata) // 2):
        if kata[i] != kata[len(kata) - 1 - i]:
            return False
    return True
kata = input("Masukkan sebuah kata: ")
if cek_palindrom(kata):
    print("True")
else:
    print("False")
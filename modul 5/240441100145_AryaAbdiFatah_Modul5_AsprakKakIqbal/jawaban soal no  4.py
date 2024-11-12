def cek_palindrom(kata):
    palindrom = ""
    for i in kata:
        palindrom = i + palindrom
        print(palindrom)
    if kata == palindrom:
        return True         #untuk melakukan perbandingan antara kata dengan palindrom sama atau tidak
    if kata != palindrom:
        return False

kata = input("masukkan kata:").lower() 
print(cek_palindrom(kata))
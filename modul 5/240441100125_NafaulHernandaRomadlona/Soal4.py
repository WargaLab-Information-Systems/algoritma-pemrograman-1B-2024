def cek_palindrom(kata):
    palindrom = ""
    for i in kata:
        palindrom = i + palindrom
        print(palindrom)
    if kata == palindrom :
      return True
    if kata != palindrom :  
      return False
Kata = input("masukkan kata:".lower())
print(cek_palindrom(Kata))


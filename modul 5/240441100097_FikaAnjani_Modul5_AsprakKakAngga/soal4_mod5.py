def cek_palindrome(kata):
    return kata == kata [::-1]

kata =str(input("masukkan kata :"))
if cek_palindrome(kata) :
    print(kata,"adalah kata palindrome")
else:
    print(kata,"bukan kata palindrome")
print (cek_palindrome(kata)) 
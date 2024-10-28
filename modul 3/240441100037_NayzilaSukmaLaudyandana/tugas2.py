nomer = int(input("masukkan bilangan bulat:"))
strnomer = str(nomer)
strbalik = ""

for i in range(len(strnomer)-1,-1,-1):
    strbalik+=strnomer[i]
    
print(strbalik)
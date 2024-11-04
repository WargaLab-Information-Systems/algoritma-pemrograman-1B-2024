n = int(input("masukan nilai desimal: "))
s = ""  
while n > 0:
    r = n % 2
    s = str(r) + s
    print(s) 
    n = n // 2

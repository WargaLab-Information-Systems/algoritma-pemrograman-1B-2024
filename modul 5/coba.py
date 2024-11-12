# print("hai")
# print("hai")
# print("hai")
# print("hai")
# print("hai")

# print("...............")

# def halo():
#     print("hai")
    
    
# halo()

# #.....................
# def nama(nama):
#     print("nama saya", nama)
    
# nama("syahrul")
# nama("irsyadd")
# nama("aripppp")

# #.....................
# def tambah(a,b):
#     return a + b

# print(tambah(3,5))

# #.........................
# def luas_persegi_panjang(panjang, lebar):
#     return panjang * lebar 
# print(luas_persegi_panjang(3,5))

# #...........................

# def perkalian(x,y):
#     print("hasil perkalian:", x * y)
    
#     perkalian(5,5)

# def ganjil_genap(angka):
#     if angka % 2 == 0:
#         return "genap"
#     else:
#         return "ganjil"
# print("angka 7 adalah", ganjil_genap(7))

#lambda

# kuadrat = lambda x: x ** 2
# print("kuadrat dari 5:", kuadrat(5))

# #..........

# kali = lambda x,y: x* y
# print("hasil perkalian", kali(5,3))

# #--------------------
# def faktorial(n):
#      if n == 0:
#          return 1
#      else:
#          return n * faktorial(n-1)
     
# print("faktorial 5: ", faktorial(5))

# #---------------
# def fibonaci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonaci(n-1) + fibonaci(n-2)
    
# print("fibonaci ke 5: ", fibonaci(5))

#-----------------
# def is_prisma(n, i=2):
#     if n <= 2:
#         return n == 0:
#     return False
#     if i * i > n :
#         return True
#     return is_prisma(n, i+1)

# print("aoakah 17 adalah bilangan prisma?", is_prisma(17))

#lokal hanya bisa di def saja, global di seluruh program

# x = 1

# def fungsi():
#     x = 2
# print("dalam fungsi")

# fungsi()
# print("diluar fungsi, x")

def halo_dunia():
    print 'Halo Dunia!'
    
halo_dunia()    #Memanggil fungsi halo_dunia
# halo_dunia()    #fungsi halo_dunia dipanggil lagi


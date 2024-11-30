# def ucapan():
#     print("selamat malam")
# ucapan()

# def masukkan_data():
#     nama = str(input("masukkan nama: "))
#     NRP = str(input("masukkan NIM: "))
# def cetakSstring():
#     print("ini adalah fungsi yang mencetak string")
#     print("silahkan masukkan data")
# cetakSstring()
# masukkan_data()

# def perkalian(a, b):
#     c= a*b
#     return c
# print(perkalian(5, 20))

# f = lambda x, y, z: x + y + z
# print(f(10, 20, 30))

# def scoop(x):
#     x = 10
#     print("nilai X dalam fungsi, x = ", x)
# x = 30
# print("nilai X di luar fungsi, x =", x)
# scoop(x)

# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("---------")
# def halo ():
#     print("hello world")
#     print("hello world")
#     print("hello world")
    
# halo()

#--------
# def nama(nama):
#     print("nama saya", nama)
    
# nama("syahrul")
# nama("heema")

#------------
# def tambah (a,b): #bebas isi berapa aja
#     return a + b
# print(tambah(3, 5))

#----------
# def luasPersegi(panjang ,lebar):
#     return panjang * lebar

# print(luasPersegi(3, 5))

#-----------
# def ganjil_genap(angka):
#     if angka % 2 == 0:
#         return "genap"
#     else:
#         return "ganjil"
    
# print("angka 7 adalah", ganjil_genap (7))

#---------------
# def hitung_diskon(harga, persen_diskon):
#     diskon = harga * (persen_diskon / 100)
#     return harga - diskon
# harga_setelah_diskon =  hitung_diskon(1000, 10)

# print("harga  setelah diskon:", harga_setelah_diskon)

#--------------
#lambda

# kuadrat = lambda x : x ** 2
# print("kuadrat dari 5:", kuadrat(5))

#-----------
# kali = lambda x, y: x*y
# print ("hasil perkalian:", kali(5, 3))

#--------------
#rekursif

# def faktorial (n):
#     if n == 0:
#         return 1
#     else:
#         return n * faktorial(n-1)
    
# print("faktorial 5: ", faktorial(5))

#----------------
# def fibonaci (n):
#     if n <= 1:
#         return n
#     else:
#         return fibonaci(n-1) + fibonaci (n-2)
    
# print("fibonaci 5:", fibonaci(5))

#------------------
# def is_prisma (n, i=2):
#     if n <= 2:
#         return n == 2
#     if n % i == 0:
#         return False
#     if n * i > n:
#         return True
#     return is_prisma (n, i+1)

# print("apakah 17 bilangan prima", is_prisma(17))

#3-------------

#scope
#variable lokal
# def fungsi_lokal():
#     x= 10
#     print("dalam fungsi, x=", x)
# fungsi_lokal()

# def fungsi_global():
#     global y
#     y += 2
#     print("dalam fungsi, y= ", y)
# fungsi_global()

#----------------
x = 1

def fungsi():
    x = 2
    print("dalam fungsi, x=", x)
    
fungsi()
x= 3
print("di luar negeri, x=", x)
    
# fungsi()
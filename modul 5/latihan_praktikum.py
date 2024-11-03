# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")


# print("-----------")
# def halo():
#     print("Hello World")
#     print("Agus Memancing")
#     print("Anas Memukul")

# halo()

#-----------------------
# def nama(nama):
#     print("Nama saya",nama)

# nama("Syahrul")
# nama("Faisal")

#-----------------------
# def tambah(a,b):
#     return a + b

# print(tambah(3,5))

#-----------------------\
# def luas_persegi_panjang(panjang, lebar):
#     return panjang * lebar

# print(luas_persegi_panjang(6,5))

#-------------------------
# def perkalian(x,y):
#     print("Hasil Perkalian", x * y)

# perkalian(4,5)

#-------------------------
# def ganjil_genap(angka):
#     if angka % 2 == 0 :
#         return "Genap"
#     else :
#         return "Ganjil"
# print("Angka 7 adalah",ganjil_genap(7))

#------------------------
# def hitung_diskon(harga,persen_diskon):
#     diskon = harga * (persen_diskon / 100)
#     return harga - diskon
# harga_setelah_diskon = hitung_diskon(1000, 10)
# print("Harga Setelah Diskon : ", harga_setelah_diskon)

#-----------------Lambda----------------
kuadrat = lambda x: x ** 2
print("Kuadrat dari 5 adalah : ", kuadrat(5))

#-------------------------------------------
# kali = lambda x,y: x * y
# print("Hasil perkalian ", kali(6,5))

#----------------fungsi rekursif---------------------------
# def faktorial(n):
#     if n == 0:
#         return n * faktorial(n-1)
    
# print("Faktorial 5 : ", faktorial (5))

#------------------------------------------------------
# def fibonacci(n):
#     if n <= 1 :
#         return n
#     else :
#         return fibonacci(n-1) + fibonacci(n-2)
# print("Fibonacci Ke 5 : ", fibonacci (5))

# def is_prisma(n, i=2) :
#     if n <= 2 :
#         return n == 2
#     if n % i == 0 :
#         return False
#     if i *i >= n :
#         return True
#     return is_prisma(n,i+1) 

# print("apakah 17 Bilangan Prima?", is_prisma(17))


# Scope Variabel
# Variabel lokal

# def fungsi_lokal():
#     x = 10
#     print("Dalam Fungsi, x = ",x)
# fungsi_lokal()

# # Variabel Global
# y = 5
# def fungsi_global():
#     global y
#     y += 2
# print("Dalam Fungsi, y= ",y)
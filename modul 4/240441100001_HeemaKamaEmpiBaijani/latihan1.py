#deklarasi variabel untuk menyimpan waktu
# waktu_persiapan = 0

# #menanyakan status makan
# status_makan = input("apakah kamu sudah makan (y/n) = ")
# if (status_makan == "n"):
#     waktu_persiapan += 15
    
# print(waktu_persiapan)

# #waktu menyakan satus mandi
# status_mandi = input("apakah kamu sudah mandi (y/n) = ")
# if (status_mandi == "n"):
#     waktu_persiapan += 10
    
# print(waktu_persiapan)

# #status kendaraan
# pilihan_kendaraan = input("menggunakan motor/ jalan kaki? = ")
# while True:
#     if (pilihan_kendaraan == "motor"):
#         waktu_transport = 15
#     elif (pilihan_kendaraan == "jalan"):
#         waktu_transport = 30
#     else:
#         print("inputan salah ulangi!")
#         pilihan_kendaraan= input("apkah mau menggunkan motor / jaaln kaki? =")
    
# #status persiapan
#     if (total_waktu <=50):
#         print(f"waktu persiapan kamu {total_waktu}")
#         print("kamu tepat waktu")
#     else:
#         print(f"waktu persiapan anda")
#         print("kamu terlambat")



#MODUL 4
#PERULANGAN BERSARANG
# for i in range (1, 4):
#     print(f"loop luar i = {i}")
#     for j in range (1, 4):
#         print(f"loop dalam j = {j}")
        
# for i in range (5):
#     for j in range (6):
#         print(f"[", i, j, "]", end= " ") #prnt menyamping
#     print()

#KOMBINASI
# a = 24
# b = 36

# while b != 0:
#     a, b = b, a%b

# print(f"faktor persekutuan terbesarnya adalah: {a}")

# a = input("masukkan nilai: ")
# for i in range(1, 10+1):
#     hasil = i * a
#     print(a, "*", i, "=", hasil)
    
#POLA MATEMATIKA
# n = 100
# a, b = 0, 1

# print("bilangan Fibonacci hingga", n)
# while a <= n:
#     print(a, end= " ")
#     a, b = b, a + b

#POLA GRAFIS
n= 5

# for i in range(1, n+1):
    
#     for j in range(n-i):
#         print(' ', end=' ')
        
#     for k in range(1, i+1):
#         print(k, end='')
#     print()
#uts

# waktu_persiapan = 0
 
# status_makan = input("udh makan? (y/n)")
# if (status_makan == "n"):
#      waktu_persiapan += 15
     
# status_mandi = input("kmu udh mandi? (y/n)")
# if (status_mandi == "n"):
#      waktu_persiapan += 10
     
# pilihan_transportasi = input("kmu jalan / pake motor?  ")
# while True:
#     if (pilihan_transportasi == "motor"):
#         waktu_transport = 15
#         break
#     elif (pilihan_transportasi == "jalan"):
#         waktu_transport = 30
#         break
#     else:
#         print("salah nulis kmu! ulang ga!!")
#         pilihan_transportasi = input("kmu jalan / pake motor")
    
# total_waktu = waktu_persiapan + waktu_transport

# if (total_waktu <= 50):
#     print(f"waktu persiapan kmu {total_waktu}")
#     print("kamu telat dek!!")
# else:
#     print(f"waktu persiapan kmu {total_waktu}")
#     print("ngga ga telat sayanggg")
        

# for i in range(1, 4):
#     print(f"loop luar i = {i}")
#     for j in range (1, 4):
#         print(f"loop dalam j = {j}")
        
# for i in range(5):
#     for j in range (6):
#         print(f"[", i,j, "]", end="")
#         # print()
# waktu = 0

# # Makan
# status_makan = input("apakah sudah makan (y/n) :")
# if (status_makan == "n") :
#     waktu += 15

# # Mandi
# status_mandi = input("apakah sudah mandi (y/n) :")
# if (status_mandi == "n") :
#     waktu += 10

# #
# kendaraan = input("jalan/motor")
# while True:
#     if kendaraan == "jalan":
        
# for i in range (1,4) :
#     print(f"loop luar i = {i}")
#     for j in range (1,4) :
#         print(f"loop dalam j = {j}")

# for i in range (5) :
#     for j in range (6) :
#         print(f"[",i,j,"]", end=" ")
#     print()

# a = 24
# b = 36

# while b != 0:
#     a,b = b,a%b
    
#     print(f"faktor persekutuan terbesarnya adalah : {a}" )

# nilai = 5

# for i in range(0, 10):
#     for j in range(5):

# print("Hidup yang tidak dipertaruhkan, Tidak akan pernah dimenangkan")

# for i in range(3):  # Loop luar (3 kali)
#     for j in range(2):  # Loop dalam (2 kali)
#         print(f"i={i}, j={j}")

# a = 24
# b = 36

# while b != 0:
#     a, b = b, a % b
    
#     print(f"FPBnya adalah: {a}")

# n = 100 
# a, b = 0, 1 

# print("Bilangan Fibonacci hingga", n)
# while a <= n:
#     print(a, end=" ")
#     a, b = b, a + b


# n = 5

# for i in range(1, n+1):
    
#     for j in range(n-i):
#         print(' ', end=' ')
        
#     for k in range(1, i+1):
#         print(k, end=' ')
#     print()    
# while b != 0 :
#     a,b = b,a % b

# print(f"faktor persekutuan terbesarnya adalah: {a}")


# nilai = int(input("masukan nilai :"))
# for i in range(1,10 +1) :
#     nilai = 


# # Loop luar
# for i in range(1,4) :
#     print(f"loop luar i = {i}")

#     # Loop dalam
#     for j in range(1,4) :
#         print(f"loop dalam j = {j}")

# n = 5

# for i in range(1, n + 1) :

#     for j in range(n-i) :
#         print(" ", end=" ")

#     for k in range(1, i + 1) :
#         print(k, end=" ")
#     print()



# Mengambil input dari pengguna
N = int(input("Masukkan ukuran sisi (N): "))
karakter = input("Masukkan karakter (misalnya 'X' atau 'O'): ")

# Bagian atas belah ketupat (termasuk garis tengah)
for i in range(N):
    # Spasi awal
    print(" " * (N - i - 1), end="")
    # Pola checkerboard
    for j in range(0, 2 * i + 1): 
        if j % 2 == 0 :
            print(karakter, end="")
        else :
            print(" ", end="")
    print()  # Pindah ke baris berikutnya

# Bagian bawah belah ketupat
for i in range(N - 2, -1, -1):
    # Spasi awal
    print(" " * (N - i - 1), end="")
    # Pola checkerboard
    for j in range(0, 2 * i + 1):
        if j % 2 == 0 :
            print(karakter, end="")
        else :
            print(" ", end="")
    print()  # Pindah ke baris berikutnya

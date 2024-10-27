# # x = 'alpro B'

# # while x:
# #     print(x)
# #     x=x[1:]

# # a = 0; b = 10

# # while a<b:
# #     print(a)
# #     a = a+1

# # for i in [5,4,3,2,1]:
# #     print(i)

# # for i in range (1,10,2):
# #     print(i)


# thawal=int(input('masukan tahun awal : '))
# thakhir=int(input('masukan tahun akhir : '))

# for thawal in range(thawal, thakhir):
#     if(thawal%400==0) or (thawal%4==0) and (thawal%100 !=0):
#          print(f'{thawal} adalah tahun kabisat')
# else:
#     print(f'{thakhir} bukan tahun kabisat')

# # size = 6
# # print(f'{size} masukan size : ')

# # s = int(input('masukan size : '))
# # a = 5
# # for i in range(s):
# #     if a==s:
# #         print('*'*a)
# #         a+=3

# # x = 1
# # while x <10:
# #     if x ==7:
# #         continue
# #     print(x)
# #     x = x+1
# # else:
# #     print('Loop sudah selesai')



# # n = 10
# # for i in range(1,10):
# #     if i%2 !=0:
# #         continue
# #     print(i)

# # for i in range(5):
# #     if i ==3:
# #         pass
# #     else:
# #         print(i)


# # sisi = 20
# # count = 1
# # for i in range(sisi):
# #     print('*'*count)
# #     count+=1


# # sisi = 5
# # count = 1
# # while True:
# #     print('*'*count)
# #     count+=1

# #     if count>sisi:

# satu = [

#     '  *  ',

#     ' **  ',

#     '  *  ',

#     '  *  ',

#     '  *  ',
#     '*****',
    
   

# ]



# empat = [

#     '  *   '
#     '  **  ',

#     ' * *  ',

#     '***** ',

#     '   *  ',

#     '   *  ',

#     '   *  '

# ]



# sembilan = [

#     ' **** ',

#     '*   *',

#     '*   *',

#     ' **** ',

#     '    *',

#     '    *',

#     ' **** '

# ]


# for row in satu:

#     print(row)


# for row in empat:

#     print(row)


# for row in sembilan:

#     print(row)




# #         
# for i in range(1, 8):  # Loop from 1 to 7
#     for j in range(1, 8):  # Loop from 1 to 7
#         if j == 5 or i == 5 or j == 6 - i:
#             print("*", end="")  # Print '+' without a newline
#         else:
#             print(" ", end="")  # Print a space without a newline
#     print()  # Move to the next line after the inner loop

# print()

# # Loop untuk setiap baris dari 1 sampai 7
# for i in range(1, 8):  # range(1, 8) menghasilkan 1, 2, 3, 4, 5, 6, 7
#     # Loop untuk setiap kolom dari 1 sampai 5
#     for j in range(1, 6):  # range(1, 6) menghasilkan 1, 2, 3, 4, 5
#         # Mengecek kondisi untuk mencetak bintang
#         # Menggunakan operator 'or' untuk memeriksa apakah kita di baris 1, 4, atau 7,
#         # atau pada kolom pertama di baris mana pun yang kurang dari atau sama dengan 4,
#         # atau pada kolom terakhir (kolom 5)
#         if i == 1 or i == 4 or i == 7 or (j == 1 and i <= 4) or j == 5:
#             print("*", end="")  # Mencetak bintang tanpa berpindah baris
#         else:
#             print(" ", end="")  # Mencetak spasi tanpa berpindah baris
#     print()  # Berpindah ke baris berikutnya setelah selesai mencetak satu baris




# thawal = int(input('masukan tahun awal : '))
# thakhir = int(input('masukan tahun akhir : '))

# for thawal in range(thawal, thakhir):
#     if thawal %400==0 or thawal % 4==0 and thakhir %100 !=0:
#         print(f'{thawal} merupakan tahun kabisat')
# else:
#   print(f'{thakhir} bukan tahun kabisat')




#menentukan ganjil genap

a = 0

# while a<10:
#     a += 1
#     if a%2:
#         print(f'bilangan ganjil')



# a = int(input('masukan angka : '))
# n = int(input('masukan angka ke 2 : '))
# i = int(input('masukan angka ke 3 : '))

# hasil = a+n*a/i-n//a%i

# print(hasil)

# Meminta input dari pengguna
# angka_input = input("Masukkan angka bulat: ")

# # Memastikan input adalah angka
# if angka_input.isdigit() or (angka_input.startswith('-') and angka_input[1:].isdigit()):
#     angka_balikan = ''
    
#     # Menggunakan looping untuk membalikkan angka
#     for i in range(len(angka_input) - 1, -1, -1):
#         angka_balikan += angka_input[i]
    
#     print("Angka setelah dibalik:", angka_balikan)
# else:
#     print("Input tidak valid. Harap masukkan angka bulat.")

hari_terlambat = 0
denda_harian = 2500
denda_tambahan = 5500
total_denda = 0

while True:
    lama_sewa = int(input('masukan lama sewa DVD : '))
    hari_terlambat = int(input('berapa lama keterlambatan anda? '))
    if hari_terlambat >5 :
        total_denda = denda_harian * hari_terlambat
    print(total_denda)

    if hari_terlambat >10:
        tambahan_hari = hari_terlambat - 10
    total_denda = (tambahan_hari // 5) * denda_tambahan
    print(total_denda)
    






# list1= ['physics', 'chemistry', 1997, 2009];
# list2= [1, 2, 3, 4, 5, 6, 7];
# print("nilai list1: [3]", list1[3])
# print("nilai list2: [3:5]", list2 [3:5])

# tup= ('physics', 'chemistry', 1997, 2009);
# print(tup)
# del tup
# print ("setelah tup dihapus: ")
# print(tup)

# A = [[1, 2],
#      [3,4]]
# B = [[5, 6],
#      [7,8]]

# hasil = [[0,0],
#          [0,0]]

# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             hasil[i][j] += A[i][k] * B[k][j]
# for row in hasil:
#     print(row)

list1= ['fisika',  'kimia', 'bilogi', 1976]
print(list1)
del list1[2];
print("setelah nilai index kedua dihapus: ")
print(list1)


#LIST
# list_buah = ['apel', 'apel']
# print(list_buah[0])

# list_angka = [i for i in range (101)]
# print(list_angka)

# #menghitung rata-rata
# total = 0
# for i in list_angka:
#     total += i

# #menghiutng hasil
# hasil = total / len(list_angka) #menghitung jumlah karakter len
# print(hasil)

#menambah data dalam list
# list_hewan = ['kucing']
# list_hewan.append ('kelinci')
# for i in list_hewan:
#     print(i)

# #update data
# list_hewan[0] = 'kangguru'
# for i in list_hewan:
#     print(i)
    
# #hapus data
# list_hewan.remove('kambing')
# for i in list_hewan:
#     print(i)
    
# del list_hewan[1]
# for i in list_hewan:
#     print(i)
    
#TUPLE
# tuple_buah = ('manga', 'apel')

# tuple_buah[0] = 'anggur' #tidak dapat mengganti data
# print(tuple_buah)

#daftar belanja (studi kasus)
# daftar_belanja = []
# #menambahkan data
# def tambah_data (nama_barang, jumlah_barang):
#     daftar_belanja.append(nama_barang, jumlah_barang)
#     print(f"{nama_barang} berhasil ditambahkan")

# def tampilkan_barang():
#     print('daftar belanja')
#     for item in daftar_belanja:
#         print(f"{nama_barang} berhasil ditambahkan")
# def menu():
#     while True:
#         print("menu: ")
#         print("1. Tambah Item: ")
#         print("2. Tampilkan Item: ")
#         print("3. Ubah Data Item: ")
#         print("4. Hapus Data Item: ")
#         print("0. keluar: ")
    
#         pilihan = input('pilih menu')
#         if pilihan == '1':
#             nama_barang = input('masukkan nama barang')
#             jumlah_barang = input('jumlah barang')
#             tambah_data(nama_barang, jumlah_barang)
#             break
#         else:
#             print('inputan salah')        
      
# menu()
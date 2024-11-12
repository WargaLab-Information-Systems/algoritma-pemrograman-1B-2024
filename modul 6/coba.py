# list1 = ['physics', 'chemistry', 1997, 2000];
# list2 = [1,2,3,4,5,6,7];
# print("nilai list1[0]:", list1[0])
# print("nilai list2[1:5]", list2[1:5])






# list1 = ['physics', 'chemistry', 1997, 2000];
# print("nilai indeks ke-2 saat ini:")
# print(list1[2])
# list1[2] = 2001
# print("nilai indeks ke-2 saat ini:")
# print(list1[2])





# list1 = ['physics', 'chemistry', 1997, 2000];
# print(list1)
# del list1[2];
# print("setelah indeks ke-2 dihapus:")
# print(list1)










# tup1 = (12, 34.56);
# tup2 = ('abc', 'xyz');
# # Syntaks seperti dibawah tidak bisa diterapkan pada tuple
# # tup[0] = 100
# # Tuple hanya mengambil isi yang dimasukan kedalam tuple baru
# tup3 = tup1 + tup2
# print(tup3)








# tup = ('physics', 'chemistry', 1997, 2000);
# print(tup)
# del tup;
# print("setelah tup dihapus :")
# print(tup)











# warna = ['merah', 'biru', 'hijau']

# for i in warna:
#     for j in warna:
#         for k in warna:
#             for l in warna:
#                 print(f"kombinasi: {i}, {j}, {k}, {l}")








# A = [[1,2],
#      [3,4]]
# B = [[5,6],
#      [7,8]]
# hasil = [[0,0],
#          [0,0]]

# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             hasil[i][j] += A[i][k] * B[k][j]

# for row in hasil:
#     print(row)







# # menambah list
# hewan = ["ayam"]
# hewan.append("anjing")
# for i in hewan:
#     print(i)


# # mengapus list
# hewan.remove("anjing")
# for i in hewan:
#     print(i)




# # Tupleeee
# daftar_belanja = []

# # tambah data
# def tambah_data(nama_barang, jumlah):
#     daftar_belanja.append[(nama_barang, jumlah)]
#     print(f"{nama_barang} berhasil ditambahkan")

# def tampilkan_barang():
#     if daftar_belanja:
#         print("daftar barang")
#         for item in daftar_belanja:
#             print(f"nama barang = {item[0]}, jumlah = {item[1]}")

#     else:
#         print("daftar belanja kosong")

# def menu():
#     while True:
#         print("menu :")
#         print("1. tambah item")
#         print("2. tampilkan item")
#         print("3. ubah data item")
#         print("4. hapus data item ")
#         print("0. keluar")

#         pilihan = input("pilih menu :")
#         if pilihan == "1" :
#             nama_barang = input("masukan nama barang :")
#             jumlah = input("masukan jumlah barang :")
#             tambah_data(nama_barang, jumlah)
#             break
#         elif pilihan == "2":
#             nama_barang = input("masukan nama barang :")
#             jumlah = input("masukan jumlah barang :")
#             tambah_data(nama_barang, jumlah)
#             break
    
#         else:
#             print("salah")



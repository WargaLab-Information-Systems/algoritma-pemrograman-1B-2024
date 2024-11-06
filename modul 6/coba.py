# list_hewan = ["kucing"]
# list_hewan[0] = "dino"

# print(list_hewan)

# del list_hewan[0]


# tuple-buah = ("mangga", "aple")

daftar_belanja = []

def tambah_data(nama_barang,jumlah_barang):
    daftar_belanja.append((nama_barang,jumlah_barang))
    print(f"(nama_barang) berhasil ditambah")

def tampilkan_daftar():
    if daftar_belanja:
        print("daftar belanja: ")
        for item in daftar_belanja

def menu():
    while True:
        print("menu: ")
        print("1, tambahkan item ")
        print("2, tampilkan item")
        print("3, ubah data item")
        print("4, hapus data item ")
        print("0, keluar")
        
        pilihan = input("pilih menu: ")
        if pilihan == "1":
            nama_barang = input("masukkan nama barang")
            jumlah_barang = input("jumlah barang: ")
            tambah_data(nama_barang, jumlah_barang)
            break
        else:
            print("inputan salah !!")
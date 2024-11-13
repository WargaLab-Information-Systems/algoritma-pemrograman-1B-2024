data_peminjaman = []

def tambah_peminjaman(data_peminjaman):
    ID_Peminjam = input("Masukkan ID Peminjaman: ")
    Nama_Peminjam = input("Masukkan Nama Peminjam: ")
    Judul_Buku = input("Masukkan Judul Buku: ")
    Tanggal_Peminjaman = input("Masukkan Tanggal Peminjaman: ")

    peminjaman = (ID_Peminjam, Nama_Peminjam, Judul_Buku, Tanggal_Peminjaman)
    data_peminjaman.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan")

def tampilkan_data_peminjaman(data_peminjaman):
        for peminjaman in data_peminjaman:
            print(f"ID Peminjam: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")

def perbarui_peminjaman(data_peminjaman):
    Id_Peminjam = input("Masukkan ID Peminjam yang akan diperbarui: ")
    for i in range(len(data_peminjaman)):
        if data_peminjaman[i][0] == Id_Peminjam:
            Nama_Peminjam = input("Masukkan Nama Peminjam baru: ")
            Judul_Buku = input("Masukkan Judul Buku baru: ")
            Tanggal_Peminjaman = input("Masukkan Tanggal Peminjaman baru: ")
            data_peminjaman[i] = (Id_Peminjam, Nama_Peminjam, Judul_Buku, Tanggal_Peminjaman)
            print("Data peminjaman berhasil diperbaharui")
     

def hapus_peminjaman(data_peminjaman):
    ID_Peminjam = input("Masukkan ID Peminjaman yang akan dihapus: ")
    for i in range(len(data_peminjaman)):
        if data_peminjaman[i][0] == ID_Peminjam:
            data_peminjaman.pop(i)
            print("Data peminjaman berhasil dihapus")
       

def menu():
    while True:
        print("Pilih Menu:")
        print("1. Tambah Data Peminjam")
        print("2. Tampilkan Data Peminjam")
        print("3. Perbarui Data Peminjam")
        print("4. Hapus Data Peminjam")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_peminjaman(data_peminjaman)
        elif pilihan == "2":
            print("Data Semua Peminjaman:")
            print("Data tidak ada")
            tampilkan_data_peminjaman(data_peminjaman)
        elif pilihan == "3":
            perbarui_peminjaman(data_peminjaman)
        elif pilihan == "4":
            hapus_peminjaman(data_peminjaman)
            print("")
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")

menu()


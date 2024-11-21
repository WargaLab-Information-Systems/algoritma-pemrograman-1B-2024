def tambahkan_data_peminjaman(id, nama, judulBuku, tanggal):
    dataPeminjamanBuku.append((id, nama, judulBuku, tanggal))
    print("Data berhasil ditambahkan")
  
def tampilkan_data_peminjaman(dataPeminjamanBuku):
    print("================================")
    print("Data peminjam buku:")
    for i in dataPeminjamanBuku:
        print(f"\nID peminjaman : {i[0]}\n Nama : {i[1]}\n Judul Buku : {i[2]}\n Tanggal Peminjaman : {i[3]}")    

def update_data_peminjaman(dataPeminjamanBuku, id, nama, judulBuku, tanggal):
    for i in range(len(dataPeminjamanBuku)):
        if dataPeminjamanBuku[i][0] == id:
            dataPeminjamanBuku[i] = (id, nama, judulBuku, tanggal)
            print("Data peminjaman buku telah di update!")
            return
    print("Data tidak ditemukan")

def hapus_data_peminjaman(dataPeminjamanBuku, id):
    for data in dataPeminjamanBuku:
        if data[0] == id:    
            dataPeminjamanBuku.remove(data)
            print("Data peminjaman buku telah dihapus")
            return
    print("Data tidak ditemukan")

dataPeminjamanBuku = []
while True:
    print("================================")
    print("Menu:")
    print("1. Tambahkan peminjaman buku")
    print("2. Tampilkan peminjaman buku")
    print("3. Update peminjaman buku")
    print("4. Hapus peminjaman buku")
    print("0. Keluar:")
    print("================================")
    pilihan = input("Masukkan Pilihan menu: ")
    
    if pilihan == "1":
        id = input("Masukkan ID peminjaman: ")
        nama = input("Masukkan nama anda: ")
        judulBuku = input("Masukkan judul buku yang anda pinjam: ")  
        tanggal = input("Tanggal peminjaman: ")
        tambahkan_data_peminjaman(id, nama, judulBuku, tanggal)
        
    elif pilihan == "2":
        tampilkan_data_peminjaman(dataPeminjamanBuku)
    
    elif pilihan == "3":
        print("Update data anda")
        id = input("Masukkan ID peminjaman anda: ")
        nama = input("Masukkan nama anda: ")        
        judulBuku = input("Masukkan judul buku: ")    
        tanggal = input("Tanggal peminjaman: ")
        update_data_peminjaman(dataPeminjamanBuku, id, nama, judulBuku, tanggal)
        
    elif pilihan == "4":
        id = input("Masukkan ID peminjaman yang ingin dihapus: ")
        hapus_data_peminjaman(dataPeminjamanBuku, id)
        
    elif pilihan == "0":
        break
    
    else:
        print("Input tidak sesuai")
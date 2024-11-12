peminjaman_buku = []

def create_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman):
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_buku.append(peminjaman)
    print("Peminjaman buku berhasil ditambahkan.")

def read_peminjaman(): 
    if not peminjaman_buku:
        print("Tidak ada data peminjaman.")
        return
    for peminjaman in peminjaman_buku:
        print(f"ID Peminjaman : {peminjaman[0]}, Nama Peminjam : {peminjaman[1]}, Judul Buku : {peminjaman[2]}, Tanggal Peminjaman : {peminjaman[3]}")

def update_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman):
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_peminjaman:
            peminjaman_buku[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diperbarui.")
            return
    print("ID peminjaman tidak ditemukan.")

def delete_peminjaman(id_peminjaman):
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_peminjaman:
            del peminjaman_buku[i]
            print("Data peminjaman berhasil dihapus.")
            return
    print("ID peminjaman tidak ditemukan.")

def menu():
    while True:
        print("-x-x-x-x-x- Sistem Peminjaman Buku Perpustakaan -x-x-x-x-x-")
        print("1. Tambah Peminjaman")
        print("2. Tampilkan Semua Peminjaman")
        print("3. Perbarui Peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5) : ")
        
        if pilihan == '1':
            id_peminjaman = input("Masukkan ID Peminjaman : ")
            nama_peminjam = input("Masukkan Nama Peminjam : ")
            judul_buku = input("Masukkan Judul Buku : ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD) : ")
            create_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
        
        elif pilihan == '2':
            read_peminjaman()
        
        elif pilihan == '3':
            id_peminjaman = input("Masukkan ID Peminjaman yang ingin diperbarui : ")
            nama_peminjam = input("Masukkan Nama Peminjam baru : ")
            judul_buku = input("Masukkan Judul Buku baru : ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (YYYY-MM-DD) : ")
            update_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
        
        elif pilihan == '4':
            id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
            delete_peminjaman(id_peminjaman)
        
        elif pilihan == '5':
            print("Terima kasih! jangan lupa kembali lagi.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()
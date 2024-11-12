peminjaman_buku = []

def create_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman):
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_buku.append(peminjaman)
    print("Peminjaman buku berhasil ditambahkan.")


def read_peminjaman():
    if not peminjaman_buku:
        print("Tidak ada data peminjaman.")
    else:
        print("Data Peminjaman Buku:")
        for peminjaman in peminjaman_buku:
            print(f"ID: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")


def update_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman):
    for i, peminjaman in enumerate(peminjaman_buku):
        if peminjaman[0] == id_peminjaman:
            peminjaman_buku[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diperbarui.")
            return
    print("ID peminjaman tidak ditemukan.")


def delete_peminjaman(id_peminjaman):
    for i, peminjaman in enumerate(peminjaman_buku):
        if peminjaman[0] == id_peminjaman:
            del peminjaman_buku[i]
            print("Data peminjaman berhasil dihapus.")
            return
    print("ID peminjaman tidak ditemukan.")

def menu():
    while True:
        print("\n=== Sistem Peminjaman Buku Perpustakaan ===")
        print("1. Tambah Peminjaman")
        print("2. Tampilkan Peminjaman")
        print("3. Update Peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1-5): ")
        
        if pilihan == '1':
            id_peminjaman = input("Masukkan ID Peminjaman: ")
            nama_peminjam = input("Masukkan Nama Peminjam: ")
            judul_buku = input("Masukkan Judul Buku: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD-MM-YYYY): ")
            create_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
        
        elif pilihan == '2':
            read_peminjaman()
        
        elif pilihan == '3':
            id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (DD-MM-YYYY): ")
            update_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
        
        elif pilihan == '4':
            id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
            delete_peminjaman(id_peminjaman)
        
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan menu
menu()
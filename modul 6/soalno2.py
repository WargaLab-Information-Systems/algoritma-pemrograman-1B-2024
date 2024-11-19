data_peminjaman = []

# Fungsi menambahkan peminjaman buku (Create)
def tambah_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD-MM-YYYY): ")
    
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    data_peminjaman.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.\n")

# Fungsi menampilkan semua data peminjaman (Read)
def tampilkan_peminjaman():
    if data_peminjaman:
        print("\nData Peminjaman Buku:")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")
    else:
        print("Belum ada data peminjaman.\n")

# Fungsi memperbarui data peminjaman (Update)
def perbarui_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang akan diperbarui: ")
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (DD-MM-YYYY): ")
            
            data_peminjaman[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diperbarui.\n")
            return
    print("Data dengan ID tersebut tidak ditemukan.\n")

# Fungsi menghapus data peminjaman (Delete)
def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang akan dihapus: ")
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            data_peminjaman.pop(i)
            print("Data peminjaman berhasil dihapus.\n")
            return
    print("Data dengan ID tersebut tidak ditemukan.\n")

# Menu utama
while True:
    print("Menu:")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Semua Peminjaman")
    print("3. Perbarui Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
    
    pilihan = input("Masukkan pilihan (1-5): ")
    
    if pilihan == "1":
        tambah_peminjaman()
    elif pilihan == "2":
        tampilkan_peminjaman()
    elif pilihan == "3":
        perbarui_peminjaman()
    elif pilihan == "4":
        hapus_peminjaman()
    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")

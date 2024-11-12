# List untuk menyimpan data peminjaman
data_peminjaman = []

# Fungsi untuk menambah data peminjaman
def tambah_peminjaman():
    id_peminjaman = input("ID Peminjaman: ")
    nama_peminjam = input("Nama Peminjam: ")
    judul_buku = input("Judul Buku: ")
    tanggal_peminjaman = input("Tanggal Peminjaman (dd-mm-yyyy): ")
    
    # Menyimpan data peminjaman dalam bentuk tuple
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    data_peminjaman.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.")

# Fungsi untuk menampilkan seluruh data peminjaman
def tampilkan_peminjaman():
    if not data_peminjaman:
        print("Tidak ada data peminjaman.")
    else:
        print("Data Peminjaman Buku:")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")

# Fungsi untuk mengupdate data peminjaman
def update_peminjaman(id_peminjaman):
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Nama Peminjam Baru: ")
            judul_buku = input("Judul Buku Baru: ")
            tanggal_peminjaman = input("Tanggal Peminjaman Baru (dd-mm-yyyy): ")
            
            # Mengganti tuple lama dengan tuple baru
            data_peminjaman[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diupdate.")
            return
    print("Data peminjaman tidak ditemukan.")

# Fungsi untuk menghapus data peminjaman
def hapus_peminjaman(id_peminjaman):
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            data_peminjaman.pop(i)
            print("Data peminjaman berhasil dihapus.")
            return
    print("Data peminjaman tidak ditemukan.")

# Main program
while True:
    print("\nSistem Peminjaman Buku Perpustakaan")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_peminjaman()
    elif pilihan == "2":
        tampilkan_peminjaman()
    elif pilihan == "3":
        id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
        update_peminjaman(id_peminjaman)
    elif pilihan == "4":
        id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
        hapus_peminjaman(id_peminjaman)
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
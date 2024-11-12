data_peminjaman = []

def tambah_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    data_peminjaman.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.")

def tampilkan_peminjaman():
    if not data_peminjaman:
        print("Tidak ada data peminjaman.")
    else:
        print("Data Peminjaman Buku:")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    print()

def perbarui_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang akan diperbarui: ")
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam baru (kosongkan jika tidak ingin mengubah): ") or peminjaman[1]
            judul_buku = input("Masukkan Judul Buku baru (kosongkan jika tidak ingin mengubah): ") or peminjaman[2]
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru YYYY-MM-DD, (kosongkan jika tidak ingin mengubah): ") or peminjaman[3]
            data_peminjaman[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diperbarui.")
            return
    print("ID peminjaman tidak ditemukan.")

def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang akan dihapus: ")
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            del data_peminjaman[i]
            print("Data peminjaman berhasil dihapus.")
            return
    print("ID peminjaman tidak ditemukan.")

while True:
    print("Menu Peminjaman Buku Perpustakaan")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Semua Peminjaman")
    print("3. Perbarui Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

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
        print("Pilihan tidak valid. Silakan coba lagi.")
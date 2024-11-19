data_peminjaman = []

def tambah_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (dd-mm-yyyy): ")
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    data_peminjaman.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.")

def tampilkan_peminjaman():
    if not data_peminjaman:
        print("Tidak ada data peminjaman.")
    else:
        print("Data Peminjaman:")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")


def update_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    i = 0  
    for peminjaman in data_peminjaman:
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (dd-mm-yyyy): ")
            data_peminjaman[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diperbarui.")
            return
        i += 1  
    print("Data peminjaman dengan ID tersebut tidak ditemukan.")

def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    i = 0  
    for peminjaman in data_peminjaman:
        if peminjaman[0] == id_peminjaman:
            del data_peminjaman[i]
            print("Data peminjaman berhasil dihapus.")
            return
        i += 1  
    print("Data peminjaman dengan ID tersebut tidak ditemukan.")

while True:
    print("\nSistem Peminjaman Buku Perpustakaan")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == '1':
        tambah_peminjaman()
    elif pilihan == '2':
        tampilkan_peminjaman()
    elif pilihan == '3':
        update_peminjaman()
    elif pilihan == '4':
        hapus_peminjaman()
    elif pilihan == '5':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")


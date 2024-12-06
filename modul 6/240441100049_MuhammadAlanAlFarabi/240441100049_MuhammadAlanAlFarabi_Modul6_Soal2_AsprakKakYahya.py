data_peminjaman_buku = []

def tambah_data():
    id = input("Masukan ID Peminjaman: ")
    nama = input("Masukan nama Peminjam: ")
    judul = input("Masukan Judul buku yang dipinjam: ")
    tanggal = input("Masukan data kapan buku dipinjamkan (DD-MM-YYYY): ")

    data_peminjaman = (id, nama, judul, tanggal)
    data_peminjaman_buku.append(data_peminjaman)
    print("Data peminjaman berhasil ditambahakan.")

def tampilkan_data():
    if data_peminjaman_buku:
        print("Daftar Peminjaman Buku:")
        for peminjaman in data_peminjaman_buku:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    
    else:
        print("Tidak ada yang meminjam buku")


def update_data():
    id = input("Masukkan ID Peminjaman yang ingin diubah: ")
    for idx, peminjaman in enumerate(data_peminjaman_buku):
        if peminjaman[0] == id:
            nama = input("Masukkan Nama Peminjam baru: ")
            judul = input("Masukkan Judul Buku baru: ")
            tanggal = input("Masukkan Tanggal Peminjaman baru (DD-MM-YYYY): ")
            data_peminjaman_buku[idx] = (id, nama, judul, tanggal)
            print("Data peminjaman berhasil diperbarui!")
            return
        
    print("ID Peminjaman tidak ditemukan.")


def hapus_data():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for index, peminjaman in enumerate(data_peminjaman_buku):
        if peminjaman[0] == id_peminjaman:
            del data_peminjaman_buku[index]
            print("Peminjaman berhasil dihapus!")
            return
        
    print("ID Peminjaman tidak ditemukan.")

def main():
    while True:
        print("Sistem Peminjaman Buku Perpustakaan")
        print("1. Tambah Peminjaman")
        print("2. Tampilkan Peminjaman")
        print("3. Update Peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            tampilkan_data()
        elif pilihan == '3':
            update_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")

if __name__ == "__main__":
    main()
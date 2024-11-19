peminjaman_list = []

# Fungsi untuk menambah peminjaman  (Create)
def tambah_peminjaman():
    print("Tambah Data Peminjaman Buku")
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD-MM-YYYY): ")
    
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_list.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan!")

# Fungsi untuk membaca data peminjaman (Read)
def tampilkan_peminjaman():
    print("Data Seluruh Peminjaman Buku")
    if peminjaman_list:
        for p in peminjaman_list:
            print(f"ID Peminjaman: {p[0]}, Nama Peminjam: {p[1]}, Judul Buku: {p[2]}, Tanggal Peminjaman: {p[3]}")
    else:
        print("Belum ada data peminjaman.")

# Fungsi untuk memperbarui data peminjaman (Update)
def ubah_peminjaman():
    print("Ubah Data Peminjaman Buku")
    id_peminjaman = input("Masukkan ID Peminjaman yang akan diubah: ")
    for i, p in enumerate(peminjaman_list):
        if p[0] == id_peminjaman:
            nama_peminjam = input(f"Masukkan Nama Peminjam Baru (sebelumnya: {p[1]}): ")
            judul_buku = input(f"Masukkan Judul Buku Baru (sebelumnya: {p[2]}): ")
            tanggal_peminjaman = input(f"Masukkan Tanggal Peminjaman Baru (sebelumnya: {p[3]}): ")
            
            peminjaman_list[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diubah!")
            return
    print("Data dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menghapus data peminjaman (Delete)
def hapus_peminjaman():
    print("Hapus Data Peminjaman Buku")
    id_peminjaman = input("Masukkan ID Peminjaman yang akan dihapus: ")
    for i, p in enumerate(peminjaman_list):
        if p[0] == id_peminjaman:
            del peminjaman_list[i]
            print("Data peminjaman berhasil dihapus!")
            return
    print("Data dengan ID tersebut tidak ditemukan.")

# Menu utama
def main():
    while True:
        print("Menu:")
        print("1. Tambah Peminjaman Buku")
        print("2. Tampilkan Data Peminjaman")
        print("3. Ubah Data Peminjaman")
        print("4. Hapus Data Peminjaman")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_peminjaman()
        elif pilihan == "2":
            tampilkan_peminjaman()
        elif pilihan == "3":
            ubah_peminjaman()
        elif pilihan == "4":
            hapus_peminjaman()
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
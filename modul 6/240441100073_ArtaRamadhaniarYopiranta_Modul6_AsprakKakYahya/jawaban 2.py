peminjaman_buku = []

def tambah_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")

    # Menyimpan data peminjaman sebagai tuple dalam list
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_buku.append(peminjaman)
    print(f"\nPeminjaman buku oleh {nama_peminjam} berhasil ditambahkan.\n")

# Fungsi untuk menampilkan semua data peminjaman (Read)
def tampilkan_peminjaman():
    if peminjaman_buku:
        print("\nDaftar Peminjaman Buku:")
        for peminjaman in peminjaman_buku:
            print(f"ID Peminjaman: {peminjaman[0]}, Nama: {peminjaman[1]}, Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")
    else:
        print("\nTidak ada data peminjaman untuk ditampilkan.\n")

# Fungsi untuk memperbarui data peminjaman (Update)
def update_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diubah: ")
    for i, peminjaman in enumerate(peminjaman_buku):
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam Baru: ")
            judul_buku = input("Masukkan Judul Buku Baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman Baru (YYYY-MM-DD): ")

            # Mengupdate data peminjaman dalam list
            peminjaman_buku[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("\nData peminjaman berhasil diperbarui.\n")
            return
    print("\nID Peminjaman tidak ditemukan.\n")

# Fungsi untuk menghapus data peminjaman (Delete)
def delete_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for i, peminjaman in enumerate(peminjaman_buku):
        if peminjaman[0] == id_peminjaman:
            # Menghapus data peminjaman dari list
            del peminjaman_buku[i]
            print("\nData peminjaman berhasil dihapus.\n")
            return
    print("\nID Peminjaman tidak ditemukan.\n")

# Fungsi utama program
def main():
    while True:
        print("=== Sistem Peminjaman Buku Perpustakaan ===")
        print("1. Tambah Peminjaman Buku")
        print("2. Tampilkan Daftar Peminjaman Buku")
        print("3. Update Peminjaman Buku")
        print("4. Hapus Peminjaman Buku")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_peminjaman()
        elif pilihan == '2':
            tampilkan_peminjaman()
        elif pilihan == '3':
            update_peminjaman()
        elif pilihan == '4':
            delete_peminjaman()
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()

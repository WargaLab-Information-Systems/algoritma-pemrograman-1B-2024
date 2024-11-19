# List untuk menyimpan data peminjaman buku
peminjaman_list = []

# Fungsi untuk menambah peminjaman (Create)
def tambah_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")
    
    peminjaman_list.append((id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman))
    print("Peminjaman berhasil ditambahkan.\n")

# Fungsi untuk menampilkan semua peminjaman (Read)
def tampilkan_peminjaman():
    if not peminjaman_list:
        print("Tidak ada data peminjaman.\n")
    else:
        for peminjaman in peminjaman_list:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    print()

# Fungsi untuk memperbarui data peminjaman (Update)
def update_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diubah: ")
    for i, peminjaman in enumerate(peminjaman_list):
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (YYYY-MM-DD): ")
            peminjaman_list[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diperbarui.\n")
            return
    print("ID peminjaman tidak ditemukan.\n")

# Fungsi untuk menghapus peminjaman (Delete)
def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for i, peminjaman in enumerate(peminjaman_list):
        if peminjaman[0] == id_peminjaman:
            del peminjaman_list[i]
            print("Peminjaman berhasil dihapus.\n")
            return
    print("ID peminjaman tidak ditemukan.\n")

# Menu utama
def main():
    while True:
        print("1. Tambah Peminjaman")
        print("2. Tampilkan Daftar Peminjaman")
        print("3. Update Peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")
        
        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == '1':
            tambah_peminjaman()
        elif pilihan == '2':
            tampilkan_peminjaman()
        elif pilihan == '3':
            update_peminjaman()
        elif pilihan == '4':
            hapus_peminjaman()
        elif pilihan == '5':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 5.")

if __name__ == "__main__":
    main()

# Inisialisasi daftar peminjaman sebagai list kosong
peminjaman_buku = []

# Fungsi untuk menambah data peminjaman
def tambah_peminjaman():
    id_peminjaman = input("ID Peminjaman: ")
    nama_peminjam = input("Nama Peminjam: ")
    judul_buku = input("Judul Buku: ")
    tanggal_peminjaman = input("Tanggal Peminjaman (YYYY-MM-DD): ")

    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_buku.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.")

# Fungsi untuk menampilkan semua data peminjaman
def lihat_peminjaman():
    if not peminjaman_buku:
        print("Belum ada data peminjaman.")
    else:
        for peminjaman in peminjaman_buku:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")

# Fungsi untuk menghapus data peminjaman berdasarkan ID
def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for peminjaman in peminjaman_buku:
        if peminjaman[0] == id_peminjaman:
            peminjaman_buku.remove(peminjaman)
            print("Data peminjaman berhasil dihapus.")
            return
    print("ID tidak ditemukan.")

# Fungsi utama untuk menampilkan menu
def main():
    while True:
        print("\n1. Tambah Peminjaman")
        print("2. Lihat Peminjaman")
        print("3. Hapus Peminjaman")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            tambah_peminjaman()
        elif pilihan == '2':
            lihat_peminjaman()
        elif pilihan == '3':
            hapus_peminjaman()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem peminjaman.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
main()

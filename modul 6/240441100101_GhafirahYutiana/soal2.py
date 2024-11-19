peminjaman_buku = []

def tambah_peminjaman():
    id_peminjaman = input("ID Peminjaman: ")
    nama_peminjam = input("Nama Peminjam: ")
    judul_buku = input("Judul Buku: ")
    tanggal_peminjaman = input("Tanggal Peminjaman (YYYY-MM-DD): ")

    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_buku.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.")

def lihat_peminjaman():
    if not peminjaman_buku:
        print("Belum ada data peminjaman.")
    else:
        for peminjaman in peminjaman_buku:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")

def update_pinjaman():
   id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
   for peminjaman in peminjaman_buku:
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Nama Peminjam: ")
            judul_buku = input("Judul Buku: ")
            tanggal_peminjaman = input("Tanggal Peminjaman (YYYY-MM-DD): ")
            peminjaman_buku.remove(peminjaman)

            print("Data peminjaman berhasil diupdate.")
            return
   
def hapus_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for peminjaman in peminjaman_buku:
        if peminjaman[0] == id_peminjaman:
            peminjaman_buku.remove(peminjaman)
            return
    print("Data peminjaman berhasil dihapus.")

def main():
    while True:
        print("\n1. Tambah Peminjaman")
        print("2. Lihat Peminjaman")
        print("3. update peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            tambah_peminjaman()
        elif pilihan == '2':
            lihat_peminjaman()
        elif pilihan == '3':
            update_pinjaman()
        elif pilihan == '4':
            hapus_peminjaman()
        elif pilihan == '5':
            print("Terima kasih program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
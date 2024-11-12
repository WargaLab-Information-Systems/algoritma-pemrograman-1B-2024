data_peminjaman = []

def tambah_peminjaman():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD/MM/YYYY): ")

    peminjaman_baru = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    data_peminjaman.append(peminjaman_baru)

def tampilkan_peminjaman():

    if data_peminjaman:
        print()
        print("=====Daftar Peminjaman Buku=====")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    else:
        print("Tidak ada data peminjaman.")

def update_peminjaman():

    id_peminjaman = input("Masukkan ID Peminjaman yang akan diupdate: ")

    for peminjaman in data_peminjaman:
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (DD/MM/YYYY): ")
            data_peminjaman[data_peminjaman.index(peminjaman)] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("***Data peminjaman berhasil diupdate!***")
            return

def hapus_peminjaman():

    id_peminjaman = input("Masukkan ID Peminjaman yang akan dihapus: ")
    
    for peminjaman in data_peminjaman:
        if peminjaman[0] == id_peminjaman:
            data_peminjaman.remove(peminjaman) 
            print("***Data peminjaman berhasil dihapus!***")
            return

def main():
    while True:
        print("======= Sistem Peminjaman Buku Perpustakaan ======")
        print("1. Tambah Data Peminjaman")
        print("2. Tampilkan Data Peminjaman")
        print("3. Update Data Peminjaman")
        print("4. Hapus Data Peminjaman")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            tambah_peminjaman()
        elif pilihan == "2":
            tampilkan_peminjaman()
        elif pilihan == "3":
            update_peminjaman()
        elif pilihan == "4":
            hapus_peminjaman()
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
main()

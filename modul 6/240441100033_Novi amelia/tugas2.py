# List untuk menyimpan data peminjaman buku
peminjaman_buku = []

def tambah_peminjaman():
    #Menambahkan data peminjaman baru ke dalam list
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD/MM/YYYY): ")

    # Menyimpan data sebagai list tanpa tuple
    peminjaman = [id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman]
    peminjaman_buku.append(peminjaman)
    print("Peminjaman buku berhasil ditambahkan!")

#read
def tampilkan_peminjaman():
    #Menampilkan seluruh data peminjaman buku
    if peminjaman_buku:
        print("\nDaftar Peminjaman Buku:")
        for peminjaman in peminjaman_buku: #sampah jumlah data yang ada di peminjaman buku
            print(f"ID Peminjaman: {peminjaman[0]}")
            print(f"Nama Peminjam: {peminjaman[1]}")
            print(f"Judul Buku: {peminjaman[2]}")
            print(f"Tanggal Peminjaman: {peminjaman[3]}")
    else:
        print("\nBelum ada data peminjaman buku.")

def cari_peminjaman():
    #Mencari data peminjaman berdasarkan ID
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dicari: ")
    for peminjaman in peminjaman_buku:
        if peminjaman[0] == id_peminjaman:
            print(f"Data Ditemukan:ID Peminjaman: {peminjaman[0]}")
            print(f"Nama Peminjam: {peminjaman[1]}")
            print(f"Judul Buku: {peminjaman[2]}")
            print(f"Tanggal Peminjaman: {peminjaman[3]}")
            return
    print("ID peminjaman tidak ditemukan.")

#memperbarui
def update_peminjaman():
    #Memperbarui data peminjaman buku berdasarkan ID
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    for i, peminjaman in peminjaman_buku:     #untuk menghitung data perelemen
        if peminjaman[0] == id_peminjaman:
            print("Masukkan data baru (biarkan kosong untuk tidak mengubah):")
            nama_peminjam = input("Nama Peminjam: ")
            judul_buku = input("Judul Buku: ")
            tanggal_peminjaman = input("Tanggal Peminjaman: ")

            # Update data jika ada input baru; jika tidak, gunakan data lama
            peminjaman[1] = nama_peminjam if nama_peminjam else peminjaman[1]
            peminjaman[2] = judul_buku if judul_buku else peminjaman[2]
            peminjaman[3] = tanggal_peminjaman if tanggal_peminjaman else peminjaman[3]
            peminjaman_buku[i] = peminjaman
            print("Data peminjaman berhasil diperbarui!")
            return
    print("ID peminjaman tidak ditemukan.")

#hapus
def hapus_peminjaman():
    #Menghapus data peminjaman buku berdasarkan ID
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for peminjaman in peminjaman_buku:
        if peminjaman[0] == id_peminjaman:
            peminjaman_buku.remove(peminjaman)
            print("Peminjaman buku berhasil dihapus!")
            return
    print("ID peminjaman tidak ditemukan.")

def menu():
    #Menampilkan menu utama
    print("\n===== Sistem Peminjaman Buku Perpustakaan =====")
    print("1. Tambah Peminjaman Buku")
    print("2. Tampilkan Semua Peminjaman Buku")
    print("3. Cari Peminjaman Buku")
    print("4. Update Peminjaman Buku")
    print("5. Hapus Peminjaman Buku")
    print("6. Keluar")

def main():
    #Fungsi utama untuk menjalankan program#
    while True:
        menu()
        pilihan = input("Pilih menu (1/2/3/4/5/6): ")

        if pilihan == '1':
            tambah_peminjaman()
        elif pilihan == '2':
            tampilkan_peminjaman()
        elif pilihan == '3':
            cari_peminjaman()
        elif pilihan == '4':
            update_peminjaman()
        elif pilihan == '5':
            hapus_peminjaman()
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Menjalankan program
main()
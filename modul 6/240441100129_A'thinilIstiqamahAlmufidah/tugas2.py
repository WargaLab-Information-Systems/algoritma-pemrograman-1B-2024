data_peminjaman = []

def tampilkan_data():
    if not data_peminjaman:
        print("Belum ada data peminjaman.")
    else:
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")

def tambah_data():
    id_peminjaman = input("ID Peminjaman: ")
    nama = input("Nama Peminjam: ")
    judul_buku = input("Judul Buku: ")
    tanggal = input("Tanggal Peminjaman (yyyy-mm-dd): ")
    data_peminjaman.append((id_peminjaman, nama, judul_buku, tanggal))
    print("Data peminjaman berhasil ditambahkan.")

def update_data():
    id_peminjaman = input("ID Peminjaman yang ingin diupdate: ")
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            nama = input("Nama Peminjam baru (kosongkan jika tidak diubah): ") or peminjaman[1]
            judul_buku = input("Judul Buku baru (kosongkan jika tidak diubah): ") or peminjaman[2]
            tanggal = input("Tanggal baru (yyyy-mm-dd, kosongkan jika tidak diubah): ") or peminjaman[3]
            data_peminjaman[i] = (id_peminjaman, nama, judul_buku, tanggal)
            print("Data peminjaman berhasil diperbarui.")
            return
    print("Data peminjaman tidak ditemukan.")

def hapus_data():
    id_peminjaman = input("ID Peminjaman yang ingin dihapus: ")
    for i, peminjaman in enumerate(data_peminjaman):
        if peminjaman[0] == id_peminjaman:
            data_peminjaman.pop(i)
            print("Data peminjaman berhasil dihapus.")
            return
    print("Data peminjaman tidak ditemukan.")

while True:
    print("\n===SISTEM PEMINJAMAN BUKU PERPUSTAKAAN===")
    print("\n1. Tambah Peminjaman")
    print("2. Lihat Semua Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")

    pilihan = input("Pilih opsi: ")
    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        update_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Opsi tidak valid.")
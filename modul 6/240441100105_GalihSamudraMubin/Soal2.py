peminjaman_buku = []

def tambah_peminjaman():
    id_peminjaman = str(input("Masukkan ID Peminjaman: "))
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (DD/MM/YYYY): ")
    
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_buku.append(peminjaman)
    print("Peminjaman berhasil ditambahkan.")

def lihat_peminjaman():
    if peminjaman_buku:
        print("\nDaftar Peminjaman Buku:")
        for peminjaman in peminjaman_buku:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    else:
        print("\nBelum ada peminjaman buku.")

def update_peminjaman():
    id_peminjaman = str(input("\nMasukkan ID Peminjaman yang ingin diupdate: "))
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam baru (biarkan kosong untuk tidak mengubah): ") or peminjaman_buku[i][1]
            judul_buku = input("Masukkan Judul Buku baru (biarkan kosong untuk tidak mengubah): ") or peminjaman_buku[i][2]
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (biarkan kosong untuk tidak mengubah): ") or peminjaman_buku[i][3]
            peminjaman_buku[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("\nPeminjaman berhasil diupdate.")
            return
    print("\nID peminjaman tidak ditemukan.")

def hapus_peminjaman():
    id_peminjaman = str(input("\nMasukkan ID Peminjaman yang ingin dihapus: "))
    
    for peminjaman in peminjaman_buku:
        if peminjaman[0] == id_peminjaman:
            peminjaman_buku.remove(peminjaman)
            print("\nPeminjaman berhasil dihapus.")
            return

    print("\nID peminjaman tidak ditemukan.")

while True:
    print("\nSistem Peminjaman Buku Perpustakaan")
    print("1. Tambah Peminjaman")
    print("2. Lihat Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_peminjaman()
    elif pilihan == "2":
        lihat_peminjaman()
    elif pilihan == "3":
        update_peminjaman()
    elif pilihan == "4":
        hapus_peminjaman()
    elif pilihan == "5":
        print("\nTerima kasih! Program selesai.")
        break
    else:
        print("\nPilihan tidak valid, silakan coba lagi.")
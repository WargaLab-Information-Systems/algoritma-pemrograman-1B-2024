
# List untuk menyimpan data peminjaman dalam bentuk tuple
daftar_peminjaman = []

def tambah_peminjaman():
    print("\n=== Tambah Peminjaman Buku ===")
    id_pinjam = input("Masukkan ID Peminjaman: ")
    nama = input("Masukkan Nama Peminjam: ")
    judul = input("Masukkan Judul Buku: ")
    tanggal = input("Masukkan Tanggal Peminjaman: ")
    
    # Membuat tuple untuk data peminjaman
    peminjaman = (id_pinjam, nama, judul, tanggal)
    daftar_peminjaman.append(peminjaman)
    print("\nPeminjaman berhasil ditambahkan!")

def tampilkan_peminjaman():
    print("\n=== Daftar Peminjaman Buku ===")
    if not daftar_peminjaman:
        print("Belum ada data peminjaman")
        return
    
    for pinjam in daftar_peminjaman:
        print("\nDetail Peminjaman:")
        print(f"ID Peminjaman: {pinjam[0]}")
        print(f"Nama Peminjam: {pinjam[1]}")
        print(f"Judul Buku: {pinjam[2]}")
        print(f"Tanggal Peminjaman: {pinjam[3]}")
        print("-" * 30)

def update_peminjaman():
    print("\n=== Update Data Peminjaman ===")
    if not daftar_peminjaman:
        print("Belum ada data peminjaman")
        return
    
    id_pinjam = input("Masukkan ID Peminjaman yang akan diupdate: ")
    
    # Mencari indeks data yang akan diupdate
    indeks = -1
    for i in range(len(daftar_peminjaman)):
        if daftar_peminjaman[i][0] == id_pinjam:
            indeks = i
            break
    
    if indeks == -1:
        print("ID Peminjaman tidak ditemukan!")
        return
    
    # Meminta data baru
    print("\nMasukkan data baru:")
    nama = input("Masukkan Nama Peminjam: ")
    judul = input("Masukkan Judul Buku: ")
    tanggal = input("Masukkan Tanggal Peminjaman: ")
    
    # Membuat tuple baru dan mengganti data lama
    peminjaman_baru = (id_pinjam, nama, judul, tanggal)
    daftar_peminjaman[indeks] = peminjaman_baru
    print("\nData peminjaman berhasil diupdate!")

def hapus_peminjaman():
    print("\n=== Hapus Data Peminjaman ===")
    if not daftar_peminjaman:
        print("Belum ada data peminjaman")
        return
    
    id_pinjam = input("Masukkan ID Peminjaman yang akan dihapus: ")
    
    # Mencari data yang akan dihapus
    for i in range(len(daftar_peminjaman)):
        if daftar_peminjaman[i][0] == id_pinjam:
            del daftar_peminjaman[i]
            print("\nData peminjaman berhasil dihapus!")
            return
    
    print("ID Peminjaman tidak ditemukan!")

def menu():
    print("\n=== SISTEM PEMINJAMAN BUKU PERPUSTAKAAN ===")
    print("1. Tambah Peminjaman")
    print("2. Lihat Daftar Peminjaman") 
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
    
    pilihan = input("Masukkan pilihan (1-5): ")
    return pilihan

# Program Utama
while True:
    pilihan = menu()
    
    if pilihan == '1':
        tambah_peminjaman()
    elif pilihan == '2':
        tampilkan_peminjaman()
    elif pilihan == '3':
        update_peminjaman()
    elif pilihan == '4':
        hapus_peminjaman()
    elif pilihan == '5':
        print("\nTerima kasih telah menggunakan program ini!")
        break
    else:
        print("\nPilihan tidak valid!")
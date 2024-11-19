peminjaman_buku = []

def tambah_peminjaman():
    id_peminjaman = len(peminjaman_buku) + 1
    nama_peminjam = input("Masukkan nama peminjam: ")
    judul_buku = input("Masukkan judul buku: ")
    tanggal_peminjaman = input("Masukkan tanggal peminjaman: ")
    
    data_peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_buku.append(data_peminjaman)
    print("Data peminjaman buku berhasil ditambahkan.")

def lihat_peminjaman():
    if not peminjaman_buku:
        print("Belum ada data peminjaman buku.")
    else:
        print("Data peminjaman buku:")
        for data in peminjaman_buku:
            print(f"ID Peminjaman: {data[0]}")
            print(f"Nama Peminjam: {data[1]}")
            print(f"Judul Buku: {data[2]}")
            print(f"Tanggal Peminjaman: {data[3]}")
            print()

def perbarui_peminjaman():
    if not peminjaman_buku:
        print("Belum ada data peminjaman buku.")
    else:
        print("Data peminjaman buku:")
        for i, data in enumerate(peminjaman_buku, start=1):
            print(f"{i}. ID Peminjaman: {data[0]}, Nama Peminjam: {data[1]}, Judul Buku: {data[2]}, Tanggal Peminjaman: {data[3]}")
        
        pilih_peminjaman = int(input("Pilih ID peminjaman yang ingin diperbarui: "))
        if 1 <= pilih_peminjaman <= len(peminjaman_buku):
            index = pilih_peminjaman - 1
            id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman = peminjaman_buku[index]
            
            print(f"Data saat ini:")
            print(f"ID Peminjaman: {id_peminjaman}")
            print(f"Nama Peminjam: {nama_peminjam}")
            print(f"Judul Buku: {judul_buku}")
            print(f"Tanggal Peminjaman: {tanggal_peminjaman}")
            
            nama_baru = input(f"Masukkan nama peminjam baru (atau tekan Enter untuk tidak mengubah): ")
            judul_baru = input(f"Masukkan judul buku baru (atau tekan Enter untuk tidak mengubah): ")
            tanggal_baru = input(f"Masukkan tanggal peminjaman baru (atau tekan Enter untuk tidak mengubah): ")
            
            if nama_baru:
                nama_peminjam = nama_baru
            if judul_baru:
                judul_buku = judul_baru
            if tanggal_baru:
                tanggal_peminjaman = tanggal_baru
            
            peminjaman_buku[index] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman buku berhasil diperbarui.")
        else:
            print("ID peminjaman tidak valid.")

def hapus_peminjaman():
    if not peminjaman_buku:
        print("Belum ada data peminjaman buku.")
    else:
        print("Data peminjaman buku:")
        for i, data in enumerate(peminjaman_buku, start=1):
            print(f"{i}. ID Peminjaman: {data[0]}, Nama Peminjam: {data[1]}, Judul Buku: {data[2]}, Tanggal Peminjaman: {data[3]}")
        
        pilih_peminjaman = int(input("Pilih ID peminjaman yang ingin dihapus: "))
        if 1 <= pilih_peminjaman <= len(peminjaman_buku):
            index = pilih_peminjaman - 1
            data_terhapus = peminjaman_buku.pop(index)
            print(f"Data peminjaman dengan ID {data_terhapus[0]} berhasil dihapus.")
        else:
            print("ID peminjaman tidak valid.")

while True:
    print("Menu:")
    print("1. Tambah Peminjaman Buku")
    print("2. Lihat Daftar Peminjaman Buku")
    print("3. Perbarui Peminjaman Buku")
    print("4. Hapus Peminjaman Buku")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    
    if pilihan == "1":
        tambah_peminjaman()
    elif pilihan == "2":
        lihat_peminjaman()
    elif pilihan == "3":
        perbarui_peminjaman()
    elif pilihan == "4":
        hapus_peminjaman()
    elif pilihan == "5":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
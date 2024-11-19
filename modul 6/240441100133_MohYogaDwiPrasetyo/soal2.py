data_peminjaman = []

def tampilkan_data():
    if data_peminjaman:
        print("\nData peminjaman buku:")
        for data in data_peminjaman:
            print(f"ID: {data[0]}, Nama: {data[1]}, Judul Buku: {data[2]}, Tanggal: {data[3]}")
    else:
        print("Tidak ada data peminjaman")
    print()

def tambah_data():
    id_peminjaman = input("Masukkan ID peminjaman: ")
    nama_peminjam = input("Masukkan nama peminjam: ")
    judul_buku = input("Masukkan judul buku: ")
    tanggal_peminjaman = (input("Masukkan tanggal peminjaman (YYYY-MM-DD): "))

    # validasi format tgl
    if len(tanggal_peminjaman) == 10 and tanggal_peminjaman[4] == '-' and tanggal_peminjaman[7] == '-':
        tahun, bulan, hari = tanggal_peminjaman.split('-')
        if len(tahun) == 4 and len(bulan) == 2 and len(hari) == 2:
            int(tahun), int(bulan), int(hari)  
            data_peminjaman.append((id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman))
            print("Data berhasil ditambahkan.")
            return

    print("Format tanggal salah. Gunakan format YYYY-MM-DD.")

def perbarui_data():
    id_peminjaman = input("Masukkan ID peminjaman yang ingin diperbarui: ")
    for i in range(len(data_peminjaman)):
        if data_peminjaman[i][0] == id_peminjaman: 
            nama_peminjam = input("Masukkan nama peminjam baru (kosongkan jika tidak diubah): ") or data_peminjaman[i][1]
            judul_buku = input("Masukkan judul buku baru (kosongkan jika tidak diubah): ") or data_peminjaman[i][2]
            tanggal_peminjaman = input("Masukkan tanggal peminjaman baru (YYYY-MM-DD, kosongkan jika tidak diubah): ") or data_peminjaman[i][3]

            # validasi format tgl
            if len(tanggal_peminjaman) == 10 and tanggal_peminjaman[4] == '-' and tanggal_peminjaman[7] == '-':
                tahun, bulan, hari = tanggal_peminjaman.split('-')
                int(tahun), int(bulan), int(hari)
                data_peminjaman[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman) #perbarui
                print("Data berhasil diperbarui.")
            else:
                print("Format tanggal salah. Data tidak diubah.")
            return
    print("Data dengan ID tersebut tidak ditemukan.")

def hapus_data():
    id_peminjaman = input("Masukkan ID peminjaman yang ingin dihapus: ")
    for data in data_peminjaman:
        if data[0] == id_peminjaman:
            data_peminjaman.remove(data)
            print("Data berhasil dihapus.")
            return
    print("Data dengan ID tersebut tidak ditemukan.")

while True:
    print("\nSistem peminjaman buku perpustakaan")
    print("1. Tambah peminjaman")
    print("2. Tampilkan data peminjaman")
    print("3. Perbarui data peminjaman")
    print("4. Hapus data peminjaman")
    print("5. Keluar")
    pilihan = input("Pilih opsi: ")

    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        tampilkan_data()
    elif pilihan == '3':
        perbarui_data()
    elif pilihan == '4':
        hapus_data()
    elif pilihan == '5':
        print("terimakasih...")
        break
    else:
        print("Pilihan tidak valid.")

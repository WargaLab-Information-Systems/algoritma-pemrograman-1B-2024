# Menyimpan data peminjam
peminjam = []

# Menambahkan data peminjam (create)
def tambahkan_data():
    id = input("Masukkan ID Peminjam : ")
    nama = input("Masukkan Nama Peminjam : ")
    judul = input("Masukkan Judul Buku : ")
    tanggal = input("Masukkan Tanggal Peminjaman (dd-mm-yy) : ")

    # Menyimpan data peminjam sebagai list
    data_baru = [id, nama, judul, tanggal]
    
    peminjam.append(data_baru)
    print(f"Data peminjam dengan ID {id} berhasil ditambahkan.")

# Menampilkan data peminjam (read)
def tampilkan_data():
    if peminjam:
        print("Daftar Peminjam:")
        for data in peminjam:
            print(f"ID Peminjam: {data[0]}, Nama Peminjam: {data[1]}, Judul Buku: {data[2]}, Tanggal Peminjaman: {data[3]}")
    else:
        print("Belum ada peminjaman.")

# Mengupdate data peminjam (update)
def ubah_data():
    ubah = input("Masukkan ID Peminjam yang ingin diubah: ")
    
    # Mencari peminjam berdasarkan ID
    for data in peminjam:
        if data[0] == ubah:  
            print(f"Data Peminjam yang ditemukan: ID Peminjam: {data[0]}, Nama Peminjam: {data[1]}, "
                  f"Judul Buku: {data[2]}, Tanggal Peminjaman: {data[3]}")

            data[1] = input("Masukkan nama baru : ")  
            data[2] = input("Masukkan judul buku baru : ")  
            data[3] = input("Masukkan tanggal peminjaman baru : ") 
            
            print("Data peminjam berhasil diubah.")
            return
    
    print("ID Peminjam tidak ditemukan.")

# Menghapus data peminjam (delete)
def hapus_data():
    id_hapus = input("Masukkan ID Peminjam yang ingin dihapus: ")
    
    # Mencari dan menghapus data berdasarkan ID
    for data in peminjam:
        if data[0] == id_hapus: 
            peminjam.remove(data)
            print(f"Data peminjam dengan ID {id_hapus} berhasil dihapus.")
            return
    
    print("ID Peminjam tidak ditemukan.")

# Menu pemilihan fitur
while True:
    menu = input('''
        Program Sistem Peminjaman Buku Perpustakaan
                
                 1. Menambahkan Data Peminjam
                 2. Menampilkan Data Peminjam
                 3. Mengubah Data Peminjam
                 4. Menghapus Data Peminjam
                 5. Keluar dari Program
                
        Masukkan Menu Berdasarkan Kebutuhan (1-5) : ''')
    
    if menu == "1":
        tambahkan_data()
    elif menu == "2":
        tampilkan_data()
    elif menu == "3":
        ubah_data()
    elif menu == "4":
        hapus_data()
    elif menu == "5":
        print("Terimakasih Telah Berkunjung ke Perpustakaan.")
        break
    else:
        print("Maaf menu yang anda masukkan salah. Silahkan Coba Lagi.")
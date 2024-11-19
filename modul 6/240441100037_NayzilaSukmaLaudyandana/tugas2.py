peminjaman_buku = []
daftarbuku = [
    (1, "Type Data Python", 5),
    (2, "Perulangan Python", 3),
    (3, "Percabangan Python", 4)
]

def tambah():
    print("Daftar Buku yang Tersedia:")
    for buku in daftarbuku:
        print(f"ID: ",buku[0],", Judul: ",buku[1],", Stok: ",buku[2])
    
    id = int(input("Masukkan ID Buku yang ingin dipinjam: "))
    for buku in daftarbuku:
        if buku[0] == id:
            if buku[2] > 0:
                nama = input("Masukkan Nama Peminjam: ")
                alamat = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")
                peminjaman_buku.append((id, nama, buku[1], alamat))
                stok(id, buku[2] - 1)
                print("Peminjaman berhasil.")
                return
            else:
                print("Stok habis.")
                return
    print("ID Buku tidak ditemukan.")

def lihat():
    if not peminjaman_buku:
        print("Tidak ada data peminjaman.")
    else:
        for peminjaman in peminjaman_buku:
            print(f"ID Buku: {peminjaman[0]}, Nama: {peminjaman[1]}, Buku: {peminjaman[2]}, alamat: {peminjaman[3]}")

def ubah():
    id = int(input("Masukkan ID Peminjaman yang akan diubah: "))
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id:
            nama = input("Masukkan Nama Peminjam Baru: ")
            buku = input("Masukkan Judul Buku Baru: ")
            alamat = input("Alamat: ")
            peminjaman_buku[i] = (id, nama, buku, alamat)
            print("Peminjaman diperbarui.")
            return
    print("ID Peminjaman tidak ditemukan.")

def hapus():
    id = int(input("Masukkan ID Peminjaman yang akan dihapus: "))
    for i in range(len(peminjaman_buku)):
        if peminjaman_buku[i][0] == id:
            del peminjaman_buku[i]
            print("Peminjaman dihapus.")
            return
    print("ID Peminjaman tidak ditemukan.")

def stok(id, stok):
    for i in range(len(daftarbuku)):
        if daftarbuku[i][0] == id:
            daftarbuku[i] = (daftarbuku[i][0], daftarbuku[i][1], stok)
            return

while True:
    print("--- Perpustakaan Keliling ---")
    print("1. Tambah Peminjaman")
    print("2. Lihat Semua Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")
        
    pilihan = input("Pilih menu (1/2/3/4/5): ")
        
    if pilihan == '1':
        tambah()
    elif pilihan == '2':
        lihat()
    elif pilihan == '3':
        ubah()
    elif pilihan == '4':
        hapus()
    elif pilihan == '5':
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
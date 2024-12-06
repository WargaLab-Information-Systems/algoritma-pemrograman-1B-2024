peminjaman_buku = []

def create(id_pinjam, nama, judul_buku, tanggal):
    peminjaman_buku.append((id_pinjam, nama, judul_buku, tanggal))

def read():
    if not peminjaman_buku:
        print("Tidak ada data peminjaman buku.")
    else:
        print("\nDaftar Peminjaman Buku:")
        for pinjam in peminjaman_buku:
            print(f"ID Peminjaman: {pinjam[0]}, Nama: {pinjam[1]}, Judul Buku: {pinjam[2]}, Tanggal Peminjaman: {pinjam[3]}")
        print()

def update(id_pinjam, nama=None, judul_buku=None, tanggal=None):
    for i, pinjam in enumerate(peminjaman_buku):
        if pinjam[0] == id_pinjam:
            updated = list(pinjam)
            if nama:
                updated[1] = nama
            if judul_buku:
                updated[2] = judul_buku
            if tanggal:
                updated[3] = tanggal
            peminjaman_buku[i] = tuple(updated)
            print(f"Peminjaman dengan ID {id_pinjam} berhasil diperbarui.\n")
            break
    else:
        print("ID peminjaman tidak ditemukan.\n")

def delete(id_pinjam):
    for i, pinjam in enumerate(peminjaman_buku):
        if pinjam[0] == id_pinjam:
            del peminjaman_buku[i]
            print(f"Peminjaman dengan ID {id_pinjam} berhasil dihapus.\n")
            break
    else:
        print("ID peminjaman tidak ditemukan.\n")

def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Peminjaman Buku")
        print("2. Lihat Daftar Peminjaman Buku")
        print("3. Update Peminjaman Buku")
        print("4. Hapus Peminjaman Buku")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4/5): ")
        
        if pilihan == '1':
            id_pinjam = int(input("Masukkan ID Peminjaman: "))
            nama = input("Masukkan Nama Peminjam: ")
            judul_buku = input("Masukkan Judul Buku: ")
            tanggal = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")
            create(id_pinjam, nama, judul_buku, tanggal)
        elif pilihan == '2':
            read()
        elif pilihan == '3':
            id_pinjam = int(input("Masukkan ID Peminjaman yang ingin diperbarui: "))
            nama = input("Masukkan Nama Peminjam baru (kosongkan jika tidak diubah): ")
            judul_buku = input("Masukkan Judul Buku baru (kosongkan jika tidak diubah): ")
            tanggal = input("Masukkan Tanggal Peminjaman baru (kosongkan jika tidak diubah): ")
            update(id_pinjam, nama if nama else None, judul_buku if judul_buku else None, tanggal if tanggal else None)
        elif pilihan == '4':
            id_pinjam = int(input("Masukkan ID Peminjaman yang ingin dihapus: "))
            delete(id_pinjam)
        elif pilihan == '5':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

menu()

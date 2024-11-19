list_peminjaman_buku = []

def buat_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman):
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    list_peminjaman_buku.append(peminjaman)
    print('Peminjaman buku berhasil')

def baca_peminjaman():
    if not list_peminjaman_buku:
        print('Tidak ada peminjaman buku')
        return  # Mengembalikan jika tidak ada peminjaman
    for peminjaman in list_peminjaman_buku:
        print(f'Id peminjaman: {peminjaman[0]}, Nama peminjam: {peminjaman[1]}, Judul buku yang dipinjam: {peminjaman[2]}, Tanggal peminjaman: {peminjaman[3]}')

def ubah_peminjaman(id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman):
    for i in range(len(list_peminjaman_buku)):
        if list_peminjaman_buku[i][1] == id_peminjaman:
            list_peminjaman_buku[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print('Data berhasil diperbarui')
            # return  # Mengembalikan setelah berhasil mengubah data
            continue
    print('Id peminjaman tidak ditemukan')

def delete_peminjaman(id_peminjaman):
    for i in range(len(list_peminjaman_buku)):
        if list_peminjaman_buku[i][0] == id_peminjaman:
            del list_peminjaman_buku[i]
            print('Peminjaman berhasil dihapus')
            return  # Mengembalikan setelah berhasil menghapus data
    print('Id tidak ditemukan')

def menu():
    while True:
        print('--------PEMINJAMAN BUKU---------')
        print('1. Buat peminjaman')
        print('2. Tampilkan semua peminjaman')
        print('3. Perbarui peminjaman')
        print('4. Hapus riwayat peminjaman')
        print('5. Keluar')

        menu_option = input('Pilih menu dari 1-5: ')

        if menu_option == '1':
            id_buku = int(input('Masukkan id peminjaman: '))
            nama_peminjam = input('Masukkan nama peminjam: ')
            judul_buku = input('Masukkan judul buku yang anda pinjam: ')
            tanggal_peminjaman = input('Masukkan tanggal peminjaman: ')  # Mengubah ke input string
            buat_peminjaman(id_buku, nama_peminjam, judul_buku, tanggal_peminjaman)
        elif menu_option == '2':
            baca_peminjaman()
        elif menu_option == '3':
            id_buku = int(input('Masukkan id peminjaman yang ingin diperbarui: '))
            nama_peminjam = input('Masukkan nama peminjam baru: ')
            judul_buku = input('Masukkan judul buku yang baru: ')
            tanggal_peminjaman = input('Masukkan tanggal peminjaman baru: ')
            ubah_peminjaman(id_buku, nama_peminjam, judul_buku, tanggal_peminjaman)
        elif menu_option == '4':
            id_peminjaman = int(input('Masukkan id peminjaman yang ingin dihapus: '))
            delete_peminjaman(id_peminjaman)
        elif menu_option == '5':
            break
        else:
            print('Pilihan tidak valid')

menu()

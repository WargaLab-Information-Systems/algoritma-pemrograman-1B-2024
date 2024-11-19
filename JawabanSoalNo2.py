data_peminjaman = [
    # id_peminjaan, nama_peminjam, judul_buku, tanggal_peminjaman]
    (1, "John Doe", "Harry Potter and the", "2022-01-01"),
    (2, "Jane Smith", "To Kill a Mockingbird", "2022-01-02"),
    (3, "Bob Johnson", "1984", "2022-01-03"),
]

def show_data_peminjaman():
    print("Data Peminjaman Buku:")
    print("+----+" + "-" * 20 + "|" + "-" * 30 + "|" + "-" * 25 + "+")
    print("| ID | \tNama Peminjam\t  | \tJudul Buku\t\t | \tTanggal Peminjaman |")
    print("+----+" + "-" * 20 + "|" + "-" * 30 + "|" + "-" * 25 + "+")
    for data in data_peminjaman:
        print(f"|{str(data[0]).center(3)} | {data[1].ljust(18)} | {data[2].ljust(28)} | {data[3].ljust(23)} |")
    print("+----+" + "-" * 20 + "|" + "-" * 30 + "|" + "-" * 25 + "+")

def create_data_peminjaman():
    id_peminjaman = max(data_peminjaman, key=lambda x: x[0])[0] + 1
    nama_peminjam = input("Masukkan nama peminjam: ")
    judul_buku = input("Masukkan judul buku: ")
    tanggal_peminjaman = input("Masukkan tanggal peminjaman (YYYY-MM-DD): ")

    data_peminjaman.append((id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman))

def update_data_peminjaman():
    id_peminjaman = int(input("Masukkan ID peminjaman yang akan diupdate: "))
    peminjaman = [data for data in data_peminjaman if data[0] == id_peminjaman]
    if not peminjaman:
        print("Data peminjaman tidak ditemukan.")
        return

    data = peminjaman[0]
    index = data_peminjaman.index(data)

    nama_peminjam = input("Masukkan nama peminjam baru: ")
    judul_buku = input("Masukkan judul buku baru: ")
    tanggal_peminjaman = input("Masukkan tanggal peminjaman baru (YYYY-MM-DD): ")

    data_peminjaman[index] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)


def delete_data_peminjaman():
    id_peminjaman = int(input("Masukkan ID peminjaman yang akan dihapus: "))
    peminjaman = [data for data in data_peminjaman if data[0] == id_peminjaman]
    if not peminjaman:
        print("Data peminjaman tidak ditemukan.")
        return

    data_peminjaman.remove(peminjaman[0])

def main():
    while True:
        print("\nSistem Peminjaman Buku Perpustakaan")
        print("1. Tampilkan Data Peminjaman")
        print("2. Tambah Data Peminjaman")
        print("3. Update Data Peminjaman")
        print("4. Hapus Data Peminjaman")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1-5): ")

        if choice == "1":
            show_data_peminjaman()
        elif choice == "2":
            create_data_peminjaman()
        elif choice == "3":
            update_data_peminjaman()
        elif choice == "4":
            delete_data_peminjaman()
        elif choice == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    print("program selesai")


if __name__ == "__main__":
    main()
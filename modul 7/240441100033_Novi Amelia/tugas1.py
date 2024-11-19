# Inisialisasi dictionary untuk alat kesehatan
alat_kesehatan = {}

# Fungsi untuk menambahkan alat
def tambah_alat(): #prmtr
    nama_alat = input("Masukkan nama alat kesehatan: ")
    jumlah = int(input(f"Masukkan jumlah {nama_alat} yang dipinjam: "))
    if nama_alat in alat_kesehatan: #mengecek suatu elemen
        alat_kesehatan[nama_alat] += jumlah
    else:
        alat_kesehatan[nama_alat] = jumlah
    print(f"{jumlah} {nama_alat} berhasil ditambahkan")

# Fungsi untuk mengembalikan alat
def kembalikan_alat():
    nama_alat = input("Masukkan nama alat kesehatan yang ingin dikembalikan: ")
    jumlah = int(input(f"Masukkan jumlah {nama_alat} yang dikembalikan: "))
    if nama_alat in alat_kesehatan and alat_kesehatan[nama_alat] >= jumlah: #kecukupan
        alat_kesehatan[nama_alat] -= jumlah
        if alat_kesehatan[nama_alat] == 0: #jumalh tersisa
            del alat_kesehatan[nama_alat]  # Hapus jika jumlahnya nol #menghapus objek atau items
        print(f"{jumlah} {nama_alat} berhasil dikembalikan.")
    else:
        print(f"Gagal mengembalikan {nama_alat}. Jumlah tidak valid atau alat tidak ditemukan.")

# Fungsi untuk menukar alat
def tukar_alat():
    nama_alat_ditukar = input("Masukkan nama alat yang akan ditukar: ")
    jumlah_ditukar= int(input(f"Masukkan jumlah {nama_alat_ditukar} yang akan ditukar: "))
    nama_alat_baru = input("Masukkan nama alat baru yang ingin ditukar: ")
    jumlah_baru = int(input(f"Masukkan jumlah {nama_alat_baru} yang diterima: "))
    if nama_alat_ditukar in alat_kesehatan and alat_kesehatan[nama_alat_ditukar] >= jumlah_ditukar: #memastikan jumlah dan adanya barang
        alat_kesehatan[nama_alat_ditukar] -= jumlah_ditukar
        if alat_kesehatan[nama_alat_ditukar] == 0:
            del alat_kesehatan[nama_alat_ditukar]  # Hapus jika jumlahnya nol
        if nama_alat_baru in alat_kesehatan:   #mengecek suatu elemen
            alat_kesehatan[nama_alat_baru] += jumlah_baru
        else:
            alat_kesehatan[nama_alat_baru] = jumlah_baru
        print(f"{jumlah_ditukar} {nama_alat_ditukar} berhasil ditukar dengan {jumlah_baru} {nama_alat_baru}.")
    else:
        print(f"Gagal menukar {nama_alat_ditukar}. Jumlah tidak valid atau alat tidak ditemukan.")

# Fungsi untuk menampilkan alat yang sedang dipinjam
def tampilkan_alat():
    if alat_kesehatan:
        print("Alat kesehatan yang sedang dipinjam:")
        for alat, jumlah in alat_kesehatan.items(): #mengakses pasangan key value #perulangan setiap key dan value
            print(f"{alat}: {jumlah}")
        print()
    else:
        print("Tidak ada alat yang sedang dipinjam")

# Menu utama
while True:
    print("=== Menu ===")
    print("1. Tambah alat")
    print("2. Kembalikan alat")
    print("3. Tukar alat")
    print("4. Tampilkan alat")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_alat()
    elif pilihan == "2":
        kembalikan_alat()
    elif pilihan == "3":
        tukar_alat()
    elif pilihan == "4":
        tampilkan_alat()
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi")
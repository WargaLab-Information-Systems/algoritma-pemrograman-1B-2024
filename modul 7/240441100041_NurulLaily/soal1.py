# Dictionary untuk menyimpan jumlah alat kesehatan yang dipinjam
alat_kesehatan = {
    "Alat Pengukur Tekanan Darah": 0,
    "Termometer": 0,
    "Stetoskop": 0,
    "Inhaler": 0
}

# Fungsi untuk meminjam alat
def pinjam(nama_alat, jumlah):
    if nama_alat in alat_kesehatan:
        alat_kesehatan[nama_alat] += jumlah
        print(f"{jumlah} {nama_alat} berhasil dipinjam.")
    else:
        print(f"Alat {nama_alat} tidak ditemukan.")

# Fungsi untuk mengembalikan alat
def kembalikan(nama_alat, jumlah):
    if nama_alat in alat_kesehatan and alat_kesehatan[nama_alat] >= jumlah:
        alat_kesehatan[nama_alat] -= jumlah
        print(f"{jumlah} {nama_alat} berhasil dikembalikan.")
    else:
        print(f"Error: Jumlah alat {nama_alat} tidak cukup untuk dikembalikan.")

# Fungsi untuk menukar alat
def tukar(nama_alat_tukar, jumlah_tukar, nama_alat_tambah, jumlah_tambah):
    if nama_alat_tukar in alat_kesehatan and alat_kesehatan[nama_alat_tukar] >= jumlah_tukar:
        alat_kesehatan[nama_alat_tukar] -= jumlah_tukar
        alat_kesehatan[nama_alat_tambah] += jumlah_tambah
        print(f"{jumlah_tukar} {nama_alat_tukar} berhasil ditukar dengan {jumlah_tambah} {nama_alat_tambah}.")
    else:
        print(f"Error: Jumlah alat {nama_alat_tukar} tidak cukup untuk ditukar.")

# Fungsi untuk menampilkan status alat kesehatan yang dipinjam
def tampilkan_status():
    print("Status peminjaman alat kesehatan:")
    for alat, jumlah in alat_kesehatan.items():
        print(f"{alat}: {jumlah}")

# Program utama
print("Program Manajemen Peminjaman Alat Kesehatan")

while True:
    print("Pilih aksi:")
    print("1. Pinjam alat")
    print("2. Kembalikan alat")
    print("3. Tukar alat")
    print("4. Tampilkan status alat")
    print("5. Keluar")
    
    pilihan = input("Masukkan pilihan (1-5): ")
    
    if pilihan == '1':  # Meminjam alat
        nama_alat = input("Masukkan nama alat yang ingin dipinjam: ")
        jumlah = int(input(f"Masukkan jumlah {nama_alat} yang ingin dipinjam: "))
        pinjam(nama_alat, jumlah)
    
    elif pilihan == '2':  # Mengembalikan alat
        nama_alat = input("Masukkan nama alat yang ingin dikembalikan: ")
        jumlah = int(input(f"Masukkan jumlah {nama_alat} yang ingin dikembalikan: "))
        kembalikan(nama_alat, jumlah)
    
    elif pilihan == '3':  # Menukar alat
        alat_tukar = input("Masukkan nama alat yang ingin ditukar: ")
        jumlah_tukar = int(input(f"Masukkan jumlah {alat_tukar} yang ingin ditukar: "))
        alat_ditambah = input("Masukkan nama alat yang akan ditambah (untuk ditukar): ")
        jumlah_ditambah = int(input(f"Masukkan jumlah {alat_ditambah} yang akan ditambah: "))
        tukar(alat_tukar, jumlah_tukar, alat_ditambah, jumlah_ditambah)
    
    elif pilihan == '4':  # Menampilkan status alat
        tampilkan_status()
    
    elif pilihan == '5':  # Keluar dari program
        print("Terima kasih telah menggunakan program ini.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")

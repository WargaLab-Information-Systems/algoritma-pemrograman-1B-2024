data_siswa = []

# Fungsi untuk menambahkan siswa
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah: ")
    
    # Menentukan kelas secara otomatis berdasarkan jumlah siswa
    kelas = (len(data_siswa) // 3) + 1
    data_siswa.append({
        "Nama": nama,
        "Kelas": f"Kelas-{kelas}",
        "Asal Sekolah": asal_sekolah
    })
    print(f"Siswa {nama} berhasil ditambahkan ke Kelas-{kelas}.")

# Fungsi untuk menampilkan semua data siswa
def tampilkan_siswa():
    if not data_siswa:
        print("Belum ada data siswa.")
        return
    print("Daftar Siswa:")
    for siswa in data_siswa:
        print(f"Nama: {siswa['Nama']}, Kelas: {siswa['Kelas']}, Asal Sekolah: {siswa['Asal Sekolah']}")
    print()

# Fungsi untuk memperbarui data siswa
def perbarui_siswa():
    nama = input("Masukkan nama siswa yang ingin diperbarui: ")
    for siswa in data_siswa:
        if siswa['Nama'] == nama:
            siswa['Nama'] = input("Masukkan nama baru: ")
            siswa['Asal Sekolah'] = input("Masukkan asal sekolah baru: ")
            print(f"Data siswa {nama} berhasil diperbarui.\n")
            return
    print(f"Siswa dengan nama {nama} tidak ditemukan.\n")

# Fungsi untuk menghapus data siswa
def hapus_siswa():
    nama = input("Masukkan nama siswa yang ingin dihapus: ")
    for siswa in data_siswa:
        if siswa['Nama'] == nama:
            data_siswa.remove(siswa)
            print(f"Data siswa {nama} berhasil dihapus.\n")
            return
    print(f"Siswa dengan nama {nama} tidak ditemukan.\n")

# Fungsi utama (menu)
def menu():
    while True:
        print("=== Sistem Administrasi Gema Ripah ===")
        print("1. Tambah Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Perbarui Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            tambah_siswa()
        elif pilihan == "2":
            tampilkan_siswa()
        elif pilihan == "3":
            perbarui_siswa()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem administrasi Gema Ripah.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.\n")

# Menjalankan program
menu()

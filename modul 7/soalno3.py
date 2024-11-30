# Inisialisasi data siswa
data_siswa = {}
kelas_counter = 1  # Menyimpan nomor kelas (Kelas-1, Kelas-2, dll)
siswa_per_kelas = 0  # Menghitung jumlah siswa dalam kelas yang sedang aktif

# Fungsi untuk menambahkan siswa
def tambah_siswa():
    global siswa_per_kelas, kelas_counter
    nama = input("Masukkan nama siswa: ")
    kelas = input("Masukkan kelas siswa: ")
    asal_sekolah = input("Masukkan asal sekolah: ")

    # Jika sudah ada 3 siswa dalam kelas yang sama, buat kelas baru
    if siswa_per_kelas == 3:
        kelas_counter += 1  # Tambah nomor kelas baru
        siswa_per_kelas = 0  # Reset jumlah siswa untuk kelas baru

    # Tentukan kelas yang akan digunakan
    kelas = f"Kelas-{kelas_counter}"
      
    # Tambahkan siswa ke kelas yang ditentukan
    if kelas not in data_siswa:
        data_siswa[kelas] = []
    
    data_siswa[kelas].append({"Nama": nama, "Kelas": kelas, "Asal Sekolah": asal_sekolah})
    siswa_per_kelas += 1  # Tambah jumlah siswa di kelas yang sedang aktif
    
    print(f"Siswa {nama} berhasil ditambahkan ke {kelas}.")

# Fungsi untuk membaca data siswa
def baca_data():
    if not data_siswa:
        print("Belum ada data siswa.")
    else:
        for kelas, siswa in data_siswa.items():
            print(f"\n{kelas}:")
            for i, data in enumerate(siswa, 1):
                print(f"  {i}. Nama: {data['Nama']}, Kelas: {data['Kelas']}, Asal Sekolah: {data['Asal Sekolah']}")

# Fungsi untuk memperbarui data siswa
def perbarui_siswa():
    # Menampilkan daftar kelas yang ada
    print("\nKelas yang tersedia:")
    print(list(data_siswa.keys()))

    kelas = input("\nMasukkan nama kelas yang ingin diperbarui: ")
    
    if kelas not in data_siswa:
        print("Kelas tidak ditemukan.")
        return

    # Menampilkan siswa dalam kelas yang dipilih
    print("\nDaftar siswa:")
    for i, siswa in enumerate(data_siswa[kelas], 1):
        print(f"{i}. {siswa['Nama']}")

    # Memperbarui data siswa
    index = int(input("Masukkan nomor siswa yang ingin diperbarui: ")) - 1
    if 0 <= index < len(data_siswa[kelas]):
        siswa = data_siswa[kelas][index]
        siswa['Nama'] = input("Nama baru: ")
        siswa['Kelas'] = input("Kelas baru: ")
        siswa['Asal Sekolah'] = input("Asal sekolah baru: ")
        print("Data siswa berhasil diperbarui.")
    else:
        print("Nomor siswa tidak valid.")

# Fungsi untuk menghapus siswa
def hapus_siswa():
    # Menampilkan daftar kelas yang ada
    print("\nKelas yang tersedia:")
    print(list(data_siswa.keys()))

    kelas = input("\nMasukkan nama kelas yang ingin dihapus siswanya: ")

    if kelas not in data_siswa:
        print("Kelas tidak ditemukan.")
        return

    # Menampilkan siswa dalam kelas yang dipilih
    print("\nDaftar siswa:")
    for i, siswa in enumerate(data_siswa[kelas], 1):
        print(f"{i}. {siswa['Nama']}")

    # Menghapus siswa
    index = int(input("Masukkan nomor siswa yang ingin dihapus: ")) - 1
    if 0 <= index < len(data_siswa[kelas]):
        siswa = data_siswa[kelas].pop(index)
        print(f"Siswa {siswa['Nama']} berhasil dihapus.")
        if not data_siswa[kelas]:
            del data_siswa[kelas]
    else:
        print("Nomor siswa tidak valid.")

# Program utama
while True:
    print("\nMenu:")
    print("1. Tambah siswa")
    print("2. Baca data siswa")
    print("3. Perbarui data siswa")
    print("4. Hapus data siswa")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        baca_data()
    elif pilihan == "3":
        perbarui_siswa()
    elif pilihan == "4":
        hapus_siswa()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")

data_siswa = {}

def menu():
    print("\n=== Sistem Administrasi Gema Ripah ===")
    print("1. Tambah Siswa")
    print("2. Lihat Semua Siswa")
    print("3. Edit Data Siswa")
    print("4. Hapus Data Siswa")
    print("5. Keluar")

# Fungsi untuk menambah siswa
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah siswa: ")

    # Menentukan kelas berdasarkan jumlah siswa
    total_siswa = sum(len(siswa) for siswa in data_siswa.values())
    kelas_baru = (total_siswa // 3) + 1
    kelas_str = f"K{kelas_baru}"

    # Menambah siswa ke kelas yang sesuai
    if kelas_str not in data_siswa:
        data_siswa[kelas_str] = []
    data_siswa[kelas_str].append({"nama": nama, "asal_sekolah": asal_sekolah})

    print(f"Siswa '{nama}' telah ditambahkan ke kelas {kelas_str}.")

# Fungsi untuk menampilkan data siswa berdasarkan kelas
def tampilkan_data():
    if not data_siswa:
        print("Belum ada data siswa.")
        return

    print("=== Data Siswa ===")
    for kelas, siswa in data_siswa.items():
        print(f"Kelas {kelas}:")
        for i, info in enumerate(siswa, start=1):
            print(f"  {i}. Nama: {info['nama']}, Asal Sekolah: {info['asal_sekolah']}")

# Fungsi untuk mengupdate data siswa
def edit_siswa():
    tampilkan_data()
    if not data_siswa:
        return

    kelas = input("Masukkan kelas siswa yang akan diubah (contoh: k1): ")
    if kelas not in data_siswa:
        print("Kelas tidak ditemukan.")
        return

    nomor_siswa = input("Masukkan nomor siswa yang akan diubah: ")
    if not nomor_siswa.isdigit() or int(nomor_siswa) < 1 or int(nomor_siswa) > len(data_siswa[kelas]):
        print("Nomor siswa tidak valid.")
        return

    nomor_siswa = int(nomor_siswa) - 1
    siswa = data_siswa[kelas][nomor_siswa]
    siswa['nama'] = input(f"Nama baru (sebelumnya: {siswa['nama']}): ") or siswa['nama']
    siswa['asal_sekolah'] = input(f"Asal sekolah baru (sebelumnya: {siswa['asal_sekolah']}): ") or siswa['asal_sekolah']
    print("Data siswa berhasil diubah.")

# Fungsi untuk menghapus data siswa
def hapus_siswa():
    tampilkan_data()
    if not data_siswa:
        return

    kelas = input("\nMasukkan kelas siswa yang akan dihapus (contoh: K1): ")
    if kelas not in data_siswa:
        print("Kelas tidak ditemukan.")
        return

    nomor_siswa = input("Masukkan nomor siswa yang akan dihapus: ")
    if not nomor_siswa.isdigit() or int(nomor_siswa) < 1 or int(nomor_siswa) > len(data_siswa[kelas]):
        print("Nomor siswa tidak valid.")
        return

    nomor_siswa = int(nomor_siswa) - 1
    siswa = data_siswa[kelas].pop(nomor_siswa)
    print(f"Siswa {siswa['nama']} telah dihapus.")

    if not data_siswa[kelas]:
        del data_siswa[kelas]

def main():
    while True:
        menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_siswa()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            edit_siswa()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

main()
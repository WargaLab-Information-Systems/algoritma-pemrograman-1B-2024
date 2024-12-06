data_siswa = {}
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah siswa: ")
    plotting = input("Masukkan plotting bimbingan intensif: ")
    kelas_tersedia = None
    for kelas, siswa in data_siswa.items():
        if len(siswa) < 3:
            kelas_tersedia = kelas
            break    
    if kelas_tersedia is None:
        kelas_ke = len(data_siswa) + 1
        kelas_tersedia = f"Kelas{kelas_ke}"
        data_siswa[kelas_tersedia] = []

    data_siswa[kelas_tersedia].append({
        "nama": nama,
        "asal_sekolah": asal_sekolah,
        "plotting": plotting
    })
    print(f"Siswa {nama} berhasil ditambahkan ke {kelas_tersedia}.")

def lihat_data():
    for kelas, siswa in data_siswa.items():
        print(f"{kelas}:")
        for idx, siswa in enumerate(siswa, start=1):
            print(f"  {idx}. Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}, Plotting: {siswa['plotting']}")

def ubah_data():
    if not data_siswa:
        print("Belum ada data siswa untuk diubah.")
        return
    lihat_data()
    kelas = input("Masukkan nama kelas (contoh: Kelas1): ")
    if kelas not in data_siswa:
        print("Kelas tidak ditemukan.")
        return
    nomor = int(input("Masukkan nomor siswa yang ingin diubah: ")) - 1
    if 0 <= nomor < len(data_siswa[kelas]):
        nama_baru = input("Masukkan nama baru: ")
        asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
        plotting_baru = input("Masukkan plotting baru: ")
        data_siswa[kelas][nomor] = {
            "nama": nama_baru,
            "asal_sekolah": asal_sekolah_baru,
            "plotting": plotting_baru
        }
        print("Data berhasil diubah.")
    else:
        print("Nomor siswa tidak valid.")

def hapus_data():
    if not data_siswa:
        print("Belum ada data siswa untuk dihapus.")
        return
    lihat_data()
    kelas = input("Masukkan nama kelas (contoh: Kelas1): ")
    if kelas not in data_siswa:
        print("Kelas tidak ditemukan.")
        return
    nomor = int(input("Masukkan nomor siswa yang ingin dihapus: ")) - 1
    if 0 <= nomor < len(data_siswa[kelas]):
        siswa_hapus = data_siswa[kelas].pop(nomor)
        print(f"Siswa {siswa_hapus['nama']} berhasil dihapus.")
        
        if not data_siswa[kelas]:
            del data_siswa[kelas]
            print(f"{kelas} telah dihapus karena tidak memiliki siswa lagi.")
    else:
        print("Nomor siswa tidak valid.")

def menu():
    while True:
        print("Sistem Pengelolaan Siswa Bimbingan Intensif")
        print("1. Tambah Siswa")
        print("2. Lihat Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            tambah_siswa()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()

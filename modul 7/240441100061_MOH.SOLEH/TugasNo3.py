data_kelas = {}

def tambah_siswa():
    nama = input("Masukkan nama siswa: ").strip()
    asal_sekolah = input("Masukkan asal sekolah: ").strip()
    plotting_bimbingan = input("Masukkan plotting bimbingan intensif: ").strip()

    if not nama or not asal_sekolah or not plotting_bimbingan:
        print("Nama, asal sekolah, dan plotting bimbingan tidak boleh kosong.\n")
        return

    jumlah_siswa = sum(len(data_kelas[kelas]) for kelas in data_kelas)
    kelas_baru = f"Kelas-{(jumlah_siswa // 3) + 1}"

    if kelas_baru not in data_kelas:
        data_kelas[kelas_baru] = []
    data_kelas[kelas_baru].append({
        "nama": nama,
        "asal_sekolah": asal_sekolah,
        "plotting_bimbingan": plotting_bimbingan
    })
    print(f"Siswa {nama} berhasil ditambahkan ke {kelas_baru}.\n")

def tampilkan_data():
    if not data_kelas:
        print("Belum ada data siswa yang terdaftar.\n")
        return
    
    print("Data Siswa Berdasarkan Plotting Kelas:")
    for kelas, siswa_list in data_kelas.items():
        print(f"{kelas}:")
        for siswa in siswa_list:
            print(f"  Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}, Plotting Bimbingan: {siswa['plotting_bimbingan']}")
    print()

def perbarui_data():
    tampilkan_data()
    kelas = input("Masukkan nama kelas siswa yang ingin diubah: ")
    if kelas not in data_kelas:
        print("Kelas tidak ditemukan.\n")
        return
    
    nama = input("Masukkan nama siswa yang ingin diubah: ")
    for siswa in data_kelas[kelas]:
        if siswa["nama"].lower() == nama.lower():
            siswa["nama"] = input("Masukkan nama baru: ").strip()
            siswa["asal_sekolah"] = input("Masukkan asal sekolah baru: ").strip()
            siswa["plotting_bimbingan"] = input("Masukkan plotting bimbingan baru: ").strip()
            print("Data siswa berhasil diperbarui.\n")
            return
    print("Siswa tidak ditemukan.\n")

def hapus_data():
    tampilkan_data()
    kelas = input("Masukkan nama kelas siswa yang ingin dihapus: ")
    if kelas not in data_kelas:
        print("Kelas tidak ditemukan.\n")
        return

    nama = input("Masukkan nama siswa yang ingin dihapus: ")
    for siswa in data_kelas[kelas]:
        if siswa["nama"].lower() == nama.lower():
            data_kelas[kelas].remove(siswa)
            print("Data siswa berhasil dihapus.\n")
            # Hapus kelas jika kosong
            if not data_kelas[kelas]:
                del data_kelas[kelas]
            return
    print("Siswa tidak ditemukan.\n")

while True:
    print("=== Menu Administrasi Bimbingan ===")
    print("1. Tambah Siswa")
    print("2. Tampilkan Data Siswa")
    print("3. Perbarui Data Siswa")
    print("4. Hapus Data Siswa")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        perbarui_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.\n")
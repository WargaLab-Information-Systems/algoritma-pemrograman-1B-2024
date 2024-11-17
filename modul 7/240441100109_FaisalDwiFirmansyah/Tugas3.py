def tambah_siswa(siswa):
    nama = input("Nama Siswa: ")
    kelas = input("Kelas: ")
    sekolah = input("Asal Sekolah: ")
    plotting = input("Plotting Bimbingan: ")

    siswa_baru = {"nama": nama, "kelas": kelas, "sekolah": sekolah, "plotting": plotting}
    siswa.append(siswa_baru)
    print(f"Siswa {nama} berhasil ditambahkan!\n")

def tampilkan_siswa(siswa):
    if len(siswa) == 0:
        print("Belum ada data siswa.\n")
        return
    print("Daftar Siswa:")
    for idx, siswa_data in enumerate(siswa, 1):
        print(f"{idx}. Nama: {siswa_data['nama']}, Kelas: {siswa_data['kelas']}, Sekolah: {siswa_data['sekolah']}, Plotting: {siswa_data['plotting']}")

def ubah_siswa(siswa):
    if len(siswa) == 0:
        print("Belum ada data siswa untuk diubah.\n")
        return

    tampilkan_siswa(siswa)
    idx = int(input("Nomor siswa yang ingin diubah: ")) - 1
    if 0 <= idx < len(siswa):
        siswa_data = siswa[idx]
        siswa_data['nama'] = input(f"Nama ({siswa_data['nama']}): ") or siswa_data['nama']
        siswa_data['kelas'] = input(f"Kelas ({siswa_data['kelas']}): ") or siswa_data['kelas']
        siswa_data['sekolah'] = input(f"Sebagai Sekolah ({siswa_data['sekolah']}): ") or siswa_data['sekolah']
        siswa_data['plotting'] = input(f"Plotting Bimbingan ({siswa_data['plotting']}): ") or siswa_data['plotting']
        print("Data siswa berhasil diubah!\n")
    else:
        print("Siswa tidak ditemukan.\n")

def hapus_siswa(siswa):
    if len(siswa) == 0:
        print("Belum ada data siswa untuk dihapus.\n")
        return

    tampilkan_siswa(siswa)
    idx = int(input("Nomor siswa yang ingin dihapus: ")) - 1
    if 0 <= idx < len(siswa):
        siswa_dihapus = siswa.pop(idx)
        print(f"Siswa {siswa_dihapus['nama']} berhasil dihapus!\n")
    else:
        print("Siswa tidak ditemukan.\n")

def kelompokkan_siswa(siswa):
    kelas = {}
    for idx, siswa_data in enumerate(siswa):
        nomor_kelas = idx // 3 + 1
        nama_kelas = f"Kelas {nomor_kelas}"
        if nama_kelas not in kelas:
            kelas[nama_kelas] = []
        kelas[nama_kelas].append(siswa_data)

    print("\nPengelompokan Siswa per Kelas:")
    for nama_kelas, siswa_list in kelas.items():
        print(f"\n{nama_kelas}:")
        for siswa_data in siswa_list:
            print(f"  - {siswa_data['nama']} (Kelas: {siswa_data['kelas']}, Sekolah: {siswa_data['sekolah']}, Plotting: {siswa_data['plotting']})")

def menu():
    siswa = []
    while True:
        print("\n=== Menu ===")
        print("1. Tambah Siswa")
        print("2. Lihat Daftar Siswa")
        print("3. Ubah Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Kelompokkan Siswa per Kelas")
        print("6. Keluar")
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            tambah_siswa(siswa)
        elif pilihan == '2':
            tampilkan_siswa(siswa)
        elif pilihan == '3':
            ubah_siswa(siswa)
        elif pilihan == '4':
            hapus_siswa(siswa)
        elif pilihan == '5':
            kelompokkan_siswa(siswa)
        elif pilihan == '6':
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
menu()
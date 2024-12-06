kelas = {}

def tambah_siswa(nama, asal_sekolah, plotting):

    if plotting not in kelas:
        kelas[plotting] = []

    if len(kelas[plotting]) < 3:
        kelas[plotting].append({"nama": nama, "asal_sekolah": asal_sekolah})
        print(f"Siswa {nama} berhasil ditambahkan ke Plotting {plotting} Kelas 1.")
    else:
        nomor_kelas = len(kelas[plotting]) // 3 + 1
        kelas_baru = f"{plotting} Kelas {nomor_kelas}"
        
        if kelas_baru not in kelas:
            kelas[kelas_baru] = [{"nama": nama, "asal_sekolah": asal_sekolah}]
        else:
            kelas[kelas_baru].append({"nama": nama, "asal_sekolah": asal_sekolah})
        print(f"Siswa {nama} berhasil ditambahkan ke Plotting {kelas_baru}.")

def tampilkan_siswa():
    if not kelas:
        print("Belum ada data siswa.")
        return
    
    for nama_kelas, siswa_list in kelas.items():
        print(f"\n{nama_kelas}:")
        for index, siswa in enumerate(siswa_list, 1):
            print(f" {index}. Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")

def update_nama(nama_lama, nama_baru):

    for nama_kelas, siswa_list in kelas.items():
        for siswa in siswa_list:
            if siswa["nama"] == nama_lama:
                siswa["nama"] = nama_baru
                print(f"Nama siswa {nama_lama} telah diperbarui menjadi {nama_baru}.")
                return
    print("Siswa tidak ditemukan.")

def hapus_siswa(nama):
    
    for nama_kelas, siswa_list in kelas.items():
        for siswa in siswa_list:
            if siswa["nama"] == nama:
                siswa_list.remove(siswa)
                print(f"Siswa {nama} telah dihapus dari {nama_kelas}.")
                return
    print("Siswa tidak ditemukan.")

while True:
    print("\nMenu:")
    print("1. Tambah Siswa")
    print("2. Tampilkan Siswa")
    print("3. Update Nama Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")

    pilihan = input("Pilih opsi: ")
    
    if pilihan == "1":
        nama = input("Masukkan nama siswa: ")
        asal_sekolah = input("Masukkan asal sekolah: ")
        plotting = input("Masukkan plotting bimbingan: ")
        tambah_siswa(nama, asal_sekolah, plotting)

    elif pilihan == "2":
        tampilkan_siswa()

    elif pilihan == "3":
        nama_lama = input("Masukkan nama lama siswa: ")
        nama_baru = input("Masukkan nama baru siswa: ")
        update_nama(nama_lama, nama_baru)

    elif pilihan == "4":
        nama = input("Masukkan nama siswa yang ingin dihapus: ")
        hapus_siswa(nama)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
siswa = []  
kelas = {}  

def tambah_siswa(nama, asal_sekolah, plotting):
    kelas_terakhir = len(kelas.get(plotting, [])) // 3
    kelas_baru = f"{plotting}_{kelas_terakhir + 1}"

    if kelas_baru not in kelas:
        kelas[kelas_baru] = []

    if len(kelas[kelas_baru]) < 3:
        kelas[kelas_baru].append({
            'nama': nama,
            'asal_sekolah': asal_sekolah,
            'plotting': plotting,
            'kelas': kelas_baru
        })
        print(f"Siswa {nama} berhasil ditambahkan ke kelas {kelas_baru}.")
    else:
        kelas_baru = f"{plotting}_{len(kelas[plotting]) + 1}"
        kelas[kelas_baru] = [{
            'nama': nama,
            'asal_sekolah': asal_sekolah,
            'plotting': plotting,
            'kelas': kelas_baru
        }]
        print(f"Kelas penuh! Siswa {nama} dipindahkan ke kelas {kelas_baru}.")

def lihat_siswa(kelas_nama):
    if kelas_nama in kelas:
        print(f"Daftar siswa di kelas {kelas_nama}:")
        for siswa_data in kelas[kelas_nama]:
            print(f"Nama: {siswa_data['nama']}, Asal Sekolah: {siswa_data['asal_sekolah']}")
    else:
        print(f"Kelas {kelas_nama} tidak ditemukan.")

def update_siswa(nama_lama, nama_baru, kelas_baru=None, plotting_baru=None):
    for kelas_nama in kelas:
        for siswa_data in kelas[kelas_nama]:
            if siswa_data['nama'] == nama_lama:
                siswa_data['nama'] = nama_baru
                if kelas_baru:
                    siswa_data['kelas'] = kelas_baru
                if plotting_baru:
                    siswa_data['plotting'] = plotting_baru
                print(f"Data siswa {nama_lama} berhasil diperbarui.")
                return
    print(f"Siswa dengan nama {nama_lama} tidak ditemukan.")

def hapus_siswa(nama):
    for kelas_nama in kelas:
        for siswa_data in kelas[kelas_nama]:
            if siswa_data['nama'] == nama:
                kelas[kelas_nama].remove(siswa_data)
                print(f"Siswa {nama} berhasil dihapus.")
                return
    print(f"Siswa dengan nama {nama} tidak ditemukan.")

def tampilkan_semua_siswa():
    for kelas_nama in kelas:
        print(f"\nKelas {kelas_nama}:")
        for siswa_data in kelas[kelas_nama]:
            print(f"Nama: {siswa_data['nama']}, Asal Sekolah: {siswa_data['asal_sekolah']}, Plotting: {siswa_data['plotting']}")

def utama():
    while True:
        print("\n--- Sistem Manajemen Bimbingan ---")
        print("1. Tambah Siswa")
        print("2. Lihat Daftar Siswa di Kelas")
        print("3. Update Data Siswa")
        print("4. Hapus Siswa")
        print("5. Lihat Semua Siswa")
        print("6. Keluar")
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah siswa: ")
            plotting = input("Masukkan plotting bimbingan (misal: Matematika, Fisika, dll): ")
            tambah_siswa(nama, asal_sekolah, plotting)
        
        elif pilihan == '2':
            kelas_nama = input("Masukkan nama kelas untuk melihat siswa (misal: Matematika_1): ")
            lihat_siswa(kelas_nama)
        
        elif pilihan == '3':
            nama_lama = input("Masukkan nama siswa yang ingin diperbarui: ")
            nama_baru = input("Masukkan nama baru: ")
            kelas_baru = input("Masukkan kelas baru (kosongkan jika tidak ada perubahan): ")
            plotting_baru = input("Masukkan plotting bimbingan baru (kosongkan jika tidak ada perubahan): ")
            update_siswa(nama_lama, nama_baru, kelas_baru if kelas_baru else None, plotting_baru if plotting_baru else None)

        elif pilihan == '4':
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            hapus_siswa(nama)

        elif pilihan == '5':
            tampilkan_semua_siswa()

        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

utama()

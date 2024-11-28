kelas_siswa = {}

def tambah_siswa():
    nama = input("Nama siswa: ")
    asal_sekolah = input("Asal sekolah: ")
    plotting = input("Plotting: ")

    # cari kelas dgn ruang kosong, atau buat kelas baru
    for nomor_kelas in sorted(kelas_siswa): 
        if len(kelas_siswa[nomor_kelas]) < 3:
            kelas_siswa[nomor_kelas].append({'nama': nama, 'asal_sekolah': asal_sekolah, 'plotting': plotting})
            print(f"Siswa {nama} ditambahkan ke kelas {nomor_kelas}.")
            return

    # jika semua kelas penuh, buat kelas baru
    kelas_baru = max(kelas_siswa.keys(), default=0) + 1
    kelas_siswa[kelas_baru] = [{'nama': nama, 'asal_sekolah': asal_sekolah, 'plotting': plotting}]
    print(f"Siswa {nama} ditambahkan ke kelas {kelas_baru}.")

def tampil_siswa():
    if not kelas_siswa:
        print("Belum ada daftar siswa.")
        return
    for nomor_kelas, siswa_list in kelas_siswa.items():
        print(f"\nKelas {nomor_kelas}:")
        for i, siswa in enumerate(siswa_list): 
            print(f"{i+1}. Nama: {siswa['nama']}, Asal sekolah: {siswa['asal_sekolah']}, Plotting: {siswa['plotting']}")

def update_siswa():
    kelas = int(input("Nomor kelas: "))
    if kelas not in kelas_siswa:
        print("Kelas tidak ditemukan.")
        return

    indeks = int(input("Nomor siswa: ")) - 1
    if 0 <= indeks < len(kelas_siswa[kelas]):
        siswa = kelas_siswa[kelas][indeks]

        # update data
        print("\nMasukkan nama baru (kosongkan jika tidak ingin diubah): ")
        siswa['nama'] = input(f"Nama baru: ") or siswa['nama']
        siswa['asal_sekolah'] = input(f"Asal sekolah baru: ") or siswa['asal_sekolah']
        siswa['plotting'] = input(f"Plotting baru: ") or siswa['plotting']
        print("Data siswa berhasil diubah.")
    else:
        print("Nomor siswa tidak valid.")

def hapus_siswa():
    kelas = int(input("Nomor kelas: "))
    if kelas not in kelas_siswa:
        print("Kelas tidak ditemukan.")
        return

    indeks = int(input("Nomor siswa: ")) - 1
    if 0 <= indeks < len(kelas_siswa[kelas]):
        nama = kelas_siswa[kelas][indeks]['nama'] #ambil nama
        del kelas_siswa[kelas][indeks]
        print(f"Siswa {nama} dihapus dari kelas {kelas}.")

        #hapus kelas jika kosong setelah penghapusan siswa
        if not kelas_siswa[kelas]:
            del kelas_siswa[kelas]
            return  

        # pindah siswa jika kelas masih ada ruang
        if len(kelas_siswa[kelas]) < 3:
            for nomor_kelas in sorted(kelas_siswa):
                if nomor_kelas != kelas and len(kelas_siswa[nomor_kelas]) > 0: 
                    siswa_pindah = kelas_siswa[nomor_kelas].pop(0) 
                    kelas_siswa[kelas].append(siswa_pindah)
                    if not kelas_siswa[nomor_kelas]:
                        del kelas_siswa[nomor_kelas]
                    break
    else:
        print("Nomor siswa tidak valid.")

def hapus_semua_siswa():
    tanya = input("Yakin ingin menghapus semua data? (y/n): ")
    if tanya == 'y':
        kelas_siswa.clear()
        print("Semua data berhasil dihapus")
    else:
        print("Batal menghapus data")

while True:
    print("\nMenu:")
    print("1. Tambah siswa")
    print("2. Tampilkan siswa")
    print("3. Ubah data siswa")
    print("4. Hapus siswa")
    print("5. Hapus semua data")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")
    if pilihan == '1':
        tambah_siswa()
    elif pilihan == '2':
        tampil_siswa()
    elif pilihan == '3':
        update_siswa()
    elif pilihan == '4':
        hapus_siswa()
    elif pilihan == '5':
        hapus_semua_siswa()
    elif pilihan == '6':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
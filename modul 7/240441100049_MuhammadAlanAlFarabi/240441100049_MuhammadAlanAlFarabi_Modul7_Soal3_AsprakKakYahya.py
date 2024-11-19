def tambah_siswa(siswa, kelas, nama, asal_sekolah):

    if len(siswa) % 3 == 0:
        kelas_baru = len(kelas) + 1
        kelas.append([])  
    else:
        kelas_baru = len(kelas)

    siswa_baru = {
        'nama': nama,
        'asal_sekolah': asal_sekolah,
        'kelas': kelas_baru
    }
    siswa.append(siswa_baru)
    kelas[kelas_baru - 1].append(siswa_baru)
    print(f"Siswa {nama} telah ditambahkan ke kelas {kelas_baru}.")

def lihat_data(siswa):

    if not siswa:
        print("Belum ada siswa yang terdaftar.")
    else:
        for s in siswa:
            print(f"Nama: {s['nama']}, Kelas: {s['kelas']}, Asal Sekolah: {s['asal_sekolah']}")

def update_siswa(siswa, nama_lama, nama_baru, asal_sekolah_baru):

    found = False
    for s in siswa:
        if s['nama'] == nama_lama:
            s['nama'] = nama_baru
            s['asal_sekolah'] = asal_sekolah_baru
            print(f"Data siswa {nama_lama} telah diperbarui menjadi {nama_baru}.")
            found = True
            break
    if not found:
        print(f"Siswa dengan nama {nama_lama} tidak ditemukan.")

def hapus_siswa(siswa, kelas, nama):

    found = False
    for s in siswa:
        if s['nama'] == nama:
            siswa.remove(s)
            kelas[s['kelas'] - 1].remove(s)
            print(f"Siswa {nama} telah dihapus.")
            found = True
            break
    if not found:
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

def tampilkan_kelas(kelas):

    if not kelas:
        print("Belum ada kelas yang terdaftar.")
    else:

        for i in range(len(kelas)):
            print(f"Kelas {i + 1}:")
            for s in kelas[i]:
                print(f"  - {s['nama']} (Sekolah: {s['asal_sekolah']})")
            print()

def main():

    siswa = []
    kelas = []
    
    while True:
        print("\n--- Menu ---")
        print("1. Tambah Siswa")
        print("2. Lihat Data Siswa")
        print("3. Update Siswa")
        print("4. Hapus Siswa")
        print("5. Tampilkan Kelas")
        print("6. Keluar")
        
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah: ")
            tambah_siswa(siswa, kelas, nama, asal_sekolah)
        
        elif pilihan == "2":
            lihat_data(siswa)
        
        elif pilihan == "3":
            nama_lama = input("Masukkan nama siswa yang akan diperbarui: ")
            nama_baru = input("Masukkan nama baru: ")
            asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
            update_siswa(siswa, nama_lama, nama_baru, asal_sekolah_baru)
        
        elif pilihan == "4":
            nama = input("Masukkan nama siswa yang akan dihapus: ")
            hapus_siswa(siswa, kelas, nama)
        
        elif pilihan == "5":
            tampilkan_kelas(kelas)
        
        elif pilihan == "6":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()


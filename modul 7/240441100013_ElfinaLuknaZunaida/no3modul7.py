data_siswa = {}
kapasitas_kelas = 3

def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah siswa: ")
    
    kelas = len(data_siswa) // kapasitas_kelas + 1
    
    data_siswa[nama] = {
        "kelas": f"Kelas {kelas}",
        "asal_sekolah": asal_sekolah
    }
    print(f"Siswa {nama} berhasil ditambahkan ke {data_siswa[nama]['kelas']}.")

# menampilkan
def lihat_siswa():
    print("\nDaftar Siswa Bimbingan Gema Ripah:")
    if data_siswa:
        for nama, info in data_siswa.items():
            print(f"Nama: {nama}, Kelas: {info['kelas']}, Asal Sekolah: {info['asal_sekolah']}")
    else:
        print("Belum ada data siswa yang tersimpan.")
    print()

# memperbarui 
def update_siswa():
    nama = input("Masukkan nama siswa yang akan diperbarui: ")
    if nama in data_siswa:
        asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
        data_siswa[nama]["asal_sekolah"] = asal_sekolah_baru
        print(f"Data siswa {nama} berhasil diperbarui.")
    else:
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

# menghapus
def hapus_siswa():
    nama = input("Masukkan nama siswa yang akan dihapus: ")
    if nama in data_siswa:
        del data_siswa[nama]
        print(f"Siswa {nama} berhasil dihapus.")
    else:
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

# menampilkan menu
def menu():
    while True:
        print(" Sistem Bimbingan Intensif Gema Ripah ")
        print("1. Tambah Siswa")
        print("2. Lihat Daftar Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tambah_siswa()
        elif pilihan == "2":
            lihat_siswa()
        elif pilihan == "3":
            update_siswa()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem bimbingan Gema Ripah!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

menu()


def tambah_siswa(kelas_dict, nama, kelas, sekolah):
    siswa = {"nama": nama, "sekolah": sekolah}
    if kelas not in kelas_dict:
        kelas_dict[kelas] = []
    
    if len(kelas_dict[kelas]) < 3: #untuk menghitug elemen dalam satu objek
        kelas_dict[kelas].append(siswa)
    else:
        print(f"Kelas {kelas} sudah penuh, menambahkan kelas baru.")
        kelas_baru = str(int(kelas) + 1)
        kelas_dict[kelas_baru] = [siswa]

def tampilkan_semua_siswa(kelas_dict):
    if not kelas_dict:
        print("Belum ada kelas yang tersedia.")
    else:
        for kelas, siswa_list in kelas_dict.items(): # menampilkan nilai sebelumnya items
            print(f"\nKelas {kelas}:")
            if siswa_list:
                for siswa in siswa_list:
                    print(f"  - {siswa['nama']} (Sekolah: {siswa['sekolah']})")
            else:
                print("  Kelas ini kosong.")

def update_siswa(kelas_dict, nama_lama, nama_baru, kelas, sekolah_baru):
    if kelas in kelas_dict:
        for siswa in kelas_dict[kelas]:
            if siswa['nama'] == nama_lama:
                siswa['nama'] = nama_baru
                siswa['sekolah'] = sekolah_baru
                print(f"Data siswa {nama_lama} telah diperbarui.")
                return
    print(f"Siswa {nama_lama} tidak ditemukan di kelas {kelas}.")

def hapus_siswa(kelas_dict, nama, kelas):
    if kelas in kelas_dict:
        for siswa in kelas_dict[kelas]:
            if siswa['nama'] == nama:
                kelas_dict[kelas].remove(siswa)
                print(f"Siswa {nama} telah dihapus dari kelas {kelas}.")
                return
    print(f"Siswa {nama} tidak ditemukan di kelas {kelas}.")

# Program utama
def main():
    kelas_dict = {}  # Menyimpan data kelas dan siswa

    while True:
        print("\nMenu:")
        print("1. Tambah Siswa")
        print("2. Tampilkan Semua Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            nama = input("Masukkan nama siswa: ")
            kelas = input("Masukkan kelas (1, 2, dst): ")
            sekolah = input("Masukkan asal sekolah: ")
            tambah_siswa(kelas_dict, nama, kelas, sekolah)

        elif pilihan == '2':
            tampilkan_semua_siswa(kelas_dict)

        elif pilihan == '3':
            nama_lama = input("Masukkan nama siswa yang akan diubah: ")
            nama_baru = input("Masukkan nama baru: ")
            kelas = input("Masukkan kelas siswa: ")
            sekolah_baru = input("Masukkan asal sekolah baru: ")
            update_siswa(kelas_dict, nama_lama, nama_baru, kelas, sekolah_baru)

        elif pilihan == '4':
            nama = input("Masukkan nama siswa yang akan dihapus: ")
            kelas = input("Masukkan kelas siswa: ")
            hapus_siswa(kelas_dict, nama, kelas)

        elif pilihan == '5':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

main()

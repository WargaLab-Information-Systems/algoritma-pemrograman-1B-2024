class BimbinganIntensif:
    def _init_(self):
        self.kelas = {}

    def tambah_siswa(self, nama, nomor_kelas, asal_sekolah, plotting):
        if nomor_kelas not in self.kelas:
            self.kelas[nomor_kelas] = []
        
        if len(self.kelas[nomor_kelas]) < 3:
            self.kelas[nomor_kelas].append({
                'nama': nama,
                'asal_sekolah': asal_sekolah,
                'plotting': plotting
            })
            print(f"Siswa {nama} berhasil ditambahkan ke kelas {nomor_kelas}.")
        else:
            kelas_baru = nomor_kelas + 1
            if kelas_baru not in self.kelas:
                self.kelas[kelas_baru] = []
            self.kelas[kelas_baru].append({
                'nama': nama,
                'asal_sekolah': asal_sekolah,
                'plotting': plotting
            })
            print(f"Kelas {nomor_kelas} penuh. Siswa {nama} berhasil ditambahkan ke kelas baru {kelas_baru}.")

    def lihat_siswa(self):
        if not self.kelas:
            print("Tidak ada siswa yang terdaftar.")
        else:
            for nomor_kelas, siswa_list in sorted(self.kelas.items()):
                print(f"\nKelas {nomor_kelas}:")
                for siswa in siswa_list:
                    print(f"Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}, Plotting: {siswa['plotting']}")

    def update_siswa(self, nama, nomor_kelas, nama_baru=None, asal_sekolah_baru=None, plotting_baru=None):
        for siswa in self.kelas.get(nomor_kelas, []):
            if siswa['nama'] == nama:
                if nama_baru:
                    siswa['nama'] = nama_baru
                if asal_sekolah_baru:
                    siswa['asal_sekolah'] = asal_sekolah_baru
                if plotting_baru:
                    siswa['plotting'] = plotting_baru
                print(f"Data siswa {nama} berhasil diperbarui.")
                return
        print(f"Siswa {nama} tidak ditemukan di kelas {nomor_kelas}.")

    def hapus_siswa(self, nama, nomor_kelas):
        for siswa in self.kelas.get(nomor_kelas, []):
            if siswa['nama'] == nama:
                self.kelas[nomor_kelas].remove(siswa)
                print(f"Siswa {nama} berhasil dihapus dari kelas {nomor_kelas}.")
                # Hapus kelas jika kosong
                if not self.kelas[nomor_kelas]:
                    del self.kelas[nomor_kelas]
                return
        print(f"Siswa {nama} tidak ditemukan di kelas {nomor_kelas}.")


def main():
    bimbingan = BimbinganIntensif()

    while True:
        print("\nMenu:")
        print("1. Tambah Siswa")
        print("2. Lihat Siswa")
        print("3. Update Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        try:
            if pilihan == "1":
                nama = input("Masukkan nama siswa: ")
                nomor_kelas = int(input("Masukkan kelas (nomor kelas): "))
                asal_sekolah = input("Masukkan asal sekolah: ")
                plotting = input("Masukkan plotting bimbingan: ")
                bimbingan.tambah_siswa(nama, nomor_kelas, asal_sekolah, plotting)

            elif pilihan == "2":
                bimbingan.lihat_siswa()

            elif pilihan == "3":
                nama = input("Masukkan nama siswa yang ingin diupdate: ")
                nomor_kelas = int(input("Masukkan kelas siswa yang ingin diupdate: "))
                nama_baru = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
                asal_sekolah_baru = input("Masukkan asal sekolah baru (kosongkan jika tidak diubah): ")
                plotting_baru = input("Masukkan plotting baru (kosongkan jika tidak diubah): ")
                bimbingan.update_siswa(nama, nomor_kelas, nama_baru, asal_sekolah_baru, plotting_baru)

            elif pilihan == "4":
                nama = input("Masukkan nama siswa yang ingin dihapus: ")
                nomor_kelas = int(input("Masukkan kelas siswa yang ingin dihapus: "))
                bimbingan.hapus_siswa(nama, nomor_kelas)

            elif pilihan == "5":
                print("Terima kasih, program selesai.")
                break

            else:
                print("Pilihan tidak valid, silakan pilih antara 1-5.")
        except ValueError:
            print("Input tidak valid. Pastikan memasukkan angka untuk nomor kelas.")

if _name_ == "_main_":
    main()
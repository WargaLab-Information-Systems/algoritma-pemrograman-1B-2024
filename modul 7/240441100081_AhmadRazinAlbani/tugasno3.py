# Inisialisasi data kelas
data_kelas = {}  
maks_siswa_per_kelas = 3


# Fungsi untuk menambah siswa
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah: ")
    bimbingan = input("Masukkan plotting bimbingan: ")

    # Cari kelas yang tersedia 
    for kelas, siswa in data_kelas.items():
        if len(siswa) < maks_siswa_per_kelas:
            data_kelas[kelas].append({'nama': nama, 'asal_sekolah': asal_sekolah, 'bimbingan': bimbingan})
            print(f"Siswa {nama} dimasukkan ke Kelas {kelas}.")
            return
   
    # Jika semua kelas penuh, buat kelas baru
    kelas_baru = len(data_kelas) + 1
    data_kelas[kelas_baru] = [{'nama': nama, 'asal_sekolah': asal_sekolah, 'bimbingan': bimbingan}]
    print(f"Siswa {nama} dimasukkan ke Kelas {kelas_baru}.")

# Fungsi untuk menampilkan data semua kelas
def tampilkan_kelas():
    print("\nData Kelas:")
    for kelas, siswa in data_kelas.items():
        print(f"Kelas {kelas}:")
        for i, data in enumerate(siswa, start=1):
            print(f"  {i}. Nama: {data['nama']}, Asal Sekolah: {data['asal_sekolah']}, Bimbingan: {data['bimbingan']}")
    if not data_kelas:
        print("  Tidak ada data kelas.")

# Fungsi untuk memperbarui data siswa
def perbarui_siswa():
    tampilkan_kelas()
    kelas = int(input("Masukkan nomor kelas siswa yang ingin diperbarui: "))
    if kelas in data_kelas:
        indeks = int(input("Masukkan nomor urut siswa dalam kelas tersebut: ")) - 1
        if 0 <= indeks < len(data_kelas[kelas]):
            siswa = data_kelas[kelas][indeks]
            siswa['nama'] = input(f"Nama ({siswa['nama']}): ") or siswa['nama']
            siswa['asal_sekolah'] = input(f"Asal Sekolah ({siswa['asal_sekolah']}): ") or siswa['asal_sekolah']
            siswa['bimbingan'] = input(f"Plotting Bimbingan ({siswa['bimbingan']}): ") or siswa['bimbingan']
            print("Data siswa berhasil diperbarui.")
        else:
            print("Nomor siswa tidak valid.")
    else:
        print("Kelas tidak ditemukan.")

# Fungsi untuk menghapus siswa
def hapus_siswa():
    tampilkan_kelas()
    kelas = int(input("Masukkan nomor kelas siswa yang ingin dihapus: "))
    if kelas in data_kelas:
        indeks = int(input("Masukkan nomor urut siswa dalam kelas tersebut: ")) - 1
        if 0 <= indeks < len(data_kelas[kelas]):
            siswa = data_kelas[kelas].pop(indeks)
            print(f"Siswa {siswa['nama']} berhasil dihapus.")
            # Hapus kelas jika kosong
            if not data_kelas[kelas]:
                del data_kelas[kelas]
                print(f"Kelas {kelas} dihapus karena kosong.")
        else:
            print("Nomor siswa tidak valid.")
    else:
        print("Kelas tidak ditemukan.")

# Menu utama
def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Tambahkan Data Siswa")
        print("2. Tampilkan Data Kelas")
        print("3. Perbarui Data Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_siswa()
        elif pilihan == "2":
            tampilkan_kelas()
        elif pilihan == "3":
            perbarui_siswa()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")
menu()


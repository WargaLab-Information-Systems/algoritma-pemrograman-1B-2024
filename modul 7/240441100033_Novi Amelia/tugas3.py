# Data utama: menyimpan informasi siswa per kelas
data_kelas = {}

# Fungsi untuk menambahkan siswa
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah: ")
    plotting_bimbingan = input("Masukkan plotting bimbingan intensif: ")

    if not nama or not asal_sekolah or not plotting_bimbingan: #kombinasi operator logika
        print("Nama, asal sekolah, dan plotting bimbingan tidak boleh kosong.")
        return

    # Hitung jumlah siswa di semua kelas
    jumlah_siswa = sum(len(data_kelas[kelas]) for kelas in data_kelas) #menjumlahkan #mengakses pasangan key value
    kelas_baru = f"Kelas-{jumlah_siswa // 3 + 1}"

    # Tambahkan siswa ke kelas
    if kelas_baru not in data_kelas: #operator logika #memeriksa apakah suatu elemen tidak terdapat dalam koleksi
        data_kelas[kelas_baru] = []
    data_kelas[kelas_baru].append({
        "nama": nama,
        "asal_sekolah": asal_sekolah,
        "plotting_bimbingan": plotting_bimbingan
    })
    print(f"Siswa {nama} berhasil ditambahkan ke {kelas_baru}.")

# Fungsi untuk membaca data siswa
def tampilkan_data():
    if not data_kelas: #operator logika
        print("Belum ada data siswa yang terdaftar")
        return
    
    print("Data Siswa Berdasarkan Plotting Kelas:")
    for kelas, siswa_list in data_kelas.items() :  #mengecek elemen #mengakses pasangan key value
        print(f"{kelas}:")
        for siswa in siswa_list:
            print(f"  Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}, Plotting Bimbingan: {siswa['plotting_bimbingan']}")
    print()

# Fungsi untuk memperbarui data siswa
def perbarui_data():
    tampilkan_data()
    kelas = input("Masukkan nama kelas siswa yang ingin diubah: ")
    if kelas not in data_kelas: #memeriksa apakah suatu elemen tidak terdapat dalam koleksi
        print("Kelas tidak ditemukan")
        return
    
    nama = input("Masukkan nama siswa yang ingin diubah: ")
    for siswa in data_kelas[kelas]:
        if siswa["nama"] == nama:
            siswa["nama"] = input("Masukkan nama baru: ")
            siswa["asal_sekolah"] = input("Masukkan asal sekolah baru: ")
            siswa["plotting_bimbingan"] = input("Masukkan plotting bimbingan baru: ")
            print("Data siswa berhasil diperbarui.")
            return
    print("Siswa tidak ditemukan.")

# Fungsi untuk menghapus data siswa
def hapus_data():
    tampilkan_data()
    kelas = input("Masukkan nama kelas siswa yang ingin dihapus: ")
    if kelas not in data_kelas: #memeriksa apakah suatu elemen tidak terdapat dalam koleksi
        print("Kelas tidak ditemukan.")
        return

    nama = input("Masukkan nama siswa yang ingin dihapus: ")
    for siswa in data_kelas[kelas]:
        if siswa["nama"] == nama:
            data_kelas[kelas].remove(siswa)
            print("Data siswa berhasil dihapus.")
            # Hapus kelas jika kosong
            if not data_kelas[kelas]:
                del data_kelas[kelas] #menghapus objek atau items
            return
    print("Siswa tidak ditemukan")

# Menu utama
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
        print("Pilihan tidak valid. Coba lagi.")
        
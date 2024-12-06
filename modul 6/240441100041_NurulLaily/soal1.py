karyawan_list = []

# Fungsi untuk menambahkan data karyawan
def tambah_karyawan():
    print("Tambah Data Karyawan")
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")

    karyawan = {"NIP": nip,
        "Nama": nama,
        "Alamat": alamat,
        "Departemen": departemen,
        "Jabatan": jabatan}

    karyawan_list.append(karyawan)
    print("Data karyawan berhasil ditambahkan!")

# Fungsi untuk mencari karyawan berdasarkan index
def cari_karyawan():
    print("Cari Data Karyawan")
    index = input("Cari berdasarkan (NIP/Nama/Alamat/Departemen/Jabatan): ")
    nilai = input(f"Masukkan {index}: ")

    hasil = [k for k in karyawan_list if k.get(index) and k[index] == nilai]

    if hasil:
        print("Data Karyawan yang Ditemukan:")
        for karyawan in hasil:
            print(f"NIP: {karyawan['NIP']}, Nama: {karyawan['Nama']}, Alamat: {karyawan['Alamat']}, "
                  f"Departemen: {karyawan['Departemen']}, Jabatan: {karyawan['Jabatan']}")
    else:
        print(f"Tidak ada data karyawan dengan {index} '{nilai}'.")

# Fungsi untuk menampilkan semua data karyawan
def tampilkan_karyawan():
    print("Data Seluruh Karyawan")
    if karyawan_list:
        for karyawan in karyawan_list:
            print(f"NIP: {karyawan['NIP']}, Nama: {karyawan['Nama']}, Alamat: {karyawan['Alamat']}, "
                  f"Departemen: {karyawan['Departemen']}, Jabatan: {karyawan['Jabatan']}")
    else:
        print("Belum ada data karyawan.")

# Menu utama
def main():
    while True:
        print("List:")
        print("1. Tambah Data Karyawan")
        print("2. Cari Data Karyawan")
        print("3. Tampilkan Seluruh Data Karyawan")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_karyawan()
        elif pilihan == "2":
            cari_karyawan()
        elif pilihan == "3":
            tampilkan_karyawan()
        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
main()
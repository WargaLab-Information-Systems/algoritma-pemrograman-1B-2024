# Menyimpan data karyawan
karyawan_list = []

# Menambahkan data karyawan
def tambah_karyawan():
    for i in range(5):
        print(f"\nKaryawan ke-{i + 1}")
        nip = input("Masukkan NIP: ")
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        departemen = input("Masukkan Departemen: ")
        jabatan = input("Masukkan Jabatan: ")
        
        # Simpan dictionary
        karyawan = {
            "NIP": nip,
            "Nama": nama,
            "Alamat": alamat,
            "Departemen": departemen,
            "Jabatan": jabatan
        }

        karyawan_list.append(karyawan)

# Mencari data karyawan
def cari_karyawan():
    atribut = input("\nCari berdasarkan (NIP, Nama, Alamat, Departemen, Jabatan): ")
    nilai = input("Masukkan nilai pencarian: ")
    
    # Hasil pencarian
    hasil = []
    for karyawan in karyawan_list:
    # Memastikan key
        if atribut in karyawan and karyawan[atribut] == nilai:
            hasil.append(karyawan)

    # Menampilkan hasil pencarian
    if hasil:
        print("\nHasil pencarian:")
        for karyawan in hasil:
            print(f"NIP: {karyawan['NIP']}, Nama: {karyawan['Nama']}, Alamat: {karyawan['Alamat']}, "
                  f"Departemen: {karyawan['Departemen']}, Jabatan: {karyawan['Jabatan']}")
    else:
        print("Tidak ada karyawan yang sesuai.")

# Fungsi utama
def main():
    tambah_karyawan()
    while True:
        cari_karyawan()
        if input("\nCari lagi? (y/n): ").lower() != 'y':
            break

# Jalankan program
main()
karyawan = []

def tambah_karyawan():
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")
    
    data_karyawan = {
        "NIP": nip,
        "Nama": nama,
        "Alamat": alamat,
        "Departemen": departemen,
        "Jabatan": jabatan
    }
    
    karyawan.append(data_karyawan)
    print("Data karyawan berhasil ditambahkan.")

def cari_karyawan():
    kata_kunci = input("Masukkan kata kunci pencarian (NIP, Nama, Alamat, Departemen, atau Jabatan): ")
    
    karyawan_cocok = []
    for data in karyawan:
        for nilai in data.values():
            if kata_kunci.lower() in str(nilai).lower():
                karyawan_cocok.append(data)
                break
    
    if karyawan_cocok:
        print("Data karyawan yang ditemukan:")
        for data in karyawan_cocok:
            print(f"NIP: {data['NIP']}")
            print(f"Nama: {data['Nama']}")
            print(f"Alamat: {data['Alamat']}")
            print(f"Departemen: {data['Departemen']}")
            print(f"Jabatan: {data['Jabatan']}")
            print()
    else:
        print("Tidak ada data karyawan yang sesuai dengan kata kunci pencarian.")

# Menambahkan minimal 5 data karyawan
for _ in range(5):
    tambah_karyawan()

while True:
    print("Menu:")
    print("1. Tambah Data Karyawan")
    print("2. Cari Data Karyawan")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == "1":
        tambah_karyawan()
    elif pilihan == "2":
        cari_karyawan()
    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
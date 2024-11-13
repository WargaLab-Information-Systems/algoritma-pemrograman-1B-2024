data_karyawan = []

def tambah_data(data_karyawan):
    NIP = input("Masukkan NIP: ")
    Nama = input("Masukkan Nama: ")
    Alamat = input("Masukkan Alamat: ")
    Departemen = input("Masukkan Departemen: ")
    Jabatan = input("Masukkan Jabatan: ")

    karyawan = [NIP, Nama, Alamat, Departemen, Jabatan]
    data_karyawan.append(karyawan)
    print("Data karyawan berhasil ditambahkan")

def cari_karyawan(data_karyawan, atribut, nilai):
    hasil_cari = []
    for karyawan in data_karyawan:
        if atribut == "NIP" and karyawan[0] == nilai:
            hasil_cari.append(karyawan)
        elif atribut == "Nama" and karyawan[1] == nilai:
            hasil_cari.append(karyawan)
        elif atribut == "Alamat" and karyawan[2] == nilai:
            hasil_cari.append(karyawan)
        elif atribut == "Departemen" and karyawan[3] == nilai:
            hasil_cari.append(karyawan)
        elif atribut == "Jabatan" and karyawan[4] == nilai:
            hasil_cari.append(karyawan)
    return hasil_cari

def tampilkan_data(data_karyawan):
        for karyawan in data_karyawan:
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def menu():
    print("Masukkan data untuk 5 karyawan")
    for i in range(5):
        tambah_data(data_karyawan)

    while True:
        print("Menu :")
        print("1. Tambah Data Karyawan")
        print("2. Cari Data Karyawan")
        print("3. Tampilkan Seluruh Data Karyawan")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_data(data_karyawan)
        elif pilihan == "2":
            atribut = input("Cari berdasarkan (NIP/Nama/Alamat/Departemen/Jabatan): ")
            nilai_yang_dicari = input(f"Masukkan {atribut} yang dicari: ")
            hasil = cari_karyawan(data_karyawan, atribut, nilai_yang_dicari)
            if hasil:
                print("Hasil Pencarian:")
                tampilkan_data(hasil)
            else:
                print(f"Tidak ditemukan data dengan {atribut} {nilai_yang_dicari}.")
        elif pilihan == "3":
            print("Semua Data Karyawan:")
            tampilkan_data(data_karyawan)
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")

menu()


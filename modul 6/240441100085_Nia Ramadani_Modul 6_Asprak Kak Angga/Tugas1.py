data_karyawan = []

def tambah_karyawan():
    print("===== MASUKKAN DATA KARYAWAN =====")
    nip = input("Masukkan NIP : ")
    nama = input("Masukkan Nama : ")
    alamat = input("Masukkan Alamat : ")
    departemen = input("Masukkan Departemen : ")
    jabatan = input("Masukkan Jabatan : ")

    karyawan = {
        "NIP": nip,
        "Nama": nama,
        "Alamat": alamat,
        "Departemen": departemen,
        "Jabatan": jabatan
    }
    
    data_karyawan.append(karyawan)
    print("Berhasil ditambahkan...")

def tampilkan_karyawan(data_karyawan):
    print("Data Karyawan : ")
    if not data_karyawan:
        print("Belum ada data karyawan yang di input..")
    else:
        for karyawan in data_karyawan:
            print(f"NIP        : {karyawan['NIP']}")
            print(f"Nama       : {karyawan['Nama']}")
            print(f"Alamat     : {karyawan['Alamat']}")
            print(f"Departemen : {karyawan['Departemen']}")
            print(f"Jabatan    : {karyawan['Jabatan']}")
            print()

def cari_karyawan(data_karyawan):
    print("===== PENCARIAN KARYAWAN =====")
    while True:
        jenis = input("Masukkan jenis pencarian (1. NIP/ 2. Nama/ 3. Alamat/ 4. Departemen/ 5. Jabatan) : ")
        if jenis == "1" :
            jenis = "NIP"
            break
        elif jenis == "2" :
            jenis = "Nama"
            break
        elif jenis == "3" :
            jenis = "Alamat"
            break
        elif jenis == "4" :
            jenis = "Departemen"
            break
        elif jenis == "5" :
            jenis = "Jabatan"
            break
        else:
            print("Input invalid....")

    nilai = input(f"Cari data {jenis} : ")

    hasil = []
    for karyawan in data_karyawan:
        if karyawan.get(jenis) and karyawan[jenis].lower() == nilai.lower():
            hasil.append(karyawan)
    
    if hasil:
        print("Hasil pencarian : ")
        for karyawan in hasil:
            print(f"  NIP        : {karyawan['NIP']}")
            print(f"  Nama       : {karyawan['Nama']}")
            print(f"  Alamat     : {karyawan['Alamat']}")
            print(f"  Departemen : {karyawan['Departemen']}")
            print(f"  Jabatan    : {karyawan['Jabatan']}")
            print()
    else:
        print("Data tidak ditemukan..")

def remove_karyawan(data_karyawan):
    print("===== HAPUS DATA =====")
    for i in range(len(data_karyawan)):
        karyawan = data_karyawan[i]
        print(f"{i + 1}. NIP: {karyawan['NIP']}, : Nama: {karyawan['Nama']}, Alamat: {karyawan['Alamat']}, Departemen: {karyawan['Departemen']}, Jabatan: {karyawan['Jabatan']}")
    
    pilihan = input("Pilih nomer yang ingin di hapus : ")
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data_karyawan):
        print("Nomer valid..")
        return
    pilihan = int(pilihan)
    del data_karyawan[pilihan - 1]
    print("Berhasil menghapus...")

while True:
    print("\n===== SELAMAT DATANG DI PT BOOKMARKET =====")
    print("1. Tambah Karyawan")
    print("2. Cari Karyawan")
    print("3. Daftar Karyawan")
    print("4. Hapus Data Karyawan")
    print("9. Keluar")
    pilih = int(input("Silahkan pilih menu : "))

    if pilih == 1:
        tambah_karyawan()
    elif pilih == 2:
        cari_karyawan(data_karyawan)
    elif pilih == 3:
        tampilkan_karyawan(data_karyawan)
    elif pilih == 4:
        remove_karyawan(data_karyawan)
    elif pilih == 9:
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

        
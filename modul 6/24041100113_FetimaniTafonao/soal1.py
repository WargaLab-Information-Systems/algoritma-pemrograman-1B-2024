karyawan_list = []

def tambah_karyawan():
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")
    karyawan_list.append((nip, nama, alamat, departemen, jabatan))
    print("Karyawan berhasil ditambahkan!\n")

def cari_karyawan():
    print("\nPencarian berdasarkan:")
    print("1. NIP\n2. Nama\n3. Alamat\n4. Departemen\n5. Jabatan")
    pilihan = input("Masukkan pilihan (1-5): ")
    nilai = input("Masukkan nilai yang dicari: ")
    ditemukan = False
    for karyawan in karyawan_list:
        if (pilihan == '1' and karyawan[0] == nilai) or \
           (pilihan == '2' and karyawan[1] == nilai) or \
           (pilihan == '3' and karyawan[2] == nilai) or \
           (pilihan == '4' and karyawan[3] == nilai) or \
           (pilihan == '5' and karyawan[4] == nilai):
            print(f"\nDitemukan: NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
            ditemukan = True
    if not ditemukan:
        print("Data tidak ditemukan.\n")

def tampilkan_semua_karyawan():
    if len(karyawan_list) == 0:
        print("\nTidak ada data karyawan.\n")
    else:
        print("\nDaftar Karyawan:")
        for karyawan in karyawan_list:
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
        print()

def menu():
    while True:
        print("\nMenu:\n1. Tambah Karyawan\n2. Cari Karyawan\n3. Tampilkan Semua Karyawan\n4. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4): ")
        if pilihan == '1':
            tambah_karyawan()
        elif pilihan == '2':
            cari_karyawan()
        elif pilihan == '3':
            tampilkan_semua_karyawan()
        elif pilihan == '4':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

menu()


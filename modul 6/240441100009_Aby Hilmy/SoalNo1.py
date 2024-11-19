def tambah_karyawan():
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")
    return {"NIP": nip, "Nama": nama, "Alamat": alamat, "Departemen": departemen, "Jabatan": jabatan}

def tampilkan_karyawan(karyawan_list):
    if len(karyawan_list) == 0:
        print("Tidak ada data karyawan.")
    else:
        for karyawan in karyawan_list:
            print(f"NIP: {karyawan['NIP']}, Nama: {karyawan['Nama']}, Alamat: {karyawan['Alamat']}, Departemen: {karyawan['Departemen']}, Jabatan: {karyawan['Jabatan']}")

def cari_karyawan(karyawan_list, atribut, nilai):
    ditemukan = False
    for karyawan in karyawan_list:
        if karyawan[atribut].lower() == nilai.lower():
            print(f"NIP: {karyawan['NIP']}, Nama: {karyawan['Nama']}, Alamat: {karyawan['Alamat']}, Departemen: {karyawan['Departemen']}, Jabatan: {karyawan['Jabatan']}")
            ditemukan = True
    if not ditemukan:
        print(f"Tidak ada karyawan dengan {atribut} '{nilai}'.")

def main():
    karyawan_list = []
    
    # Menambahkan data karyawan
    print("Masukkan data karyawan (minimal 5 karyawan):")
    for i in range(5):
        print(f"\nKaryawan ke-{i+1}")
        karyawan_list.append(tambah_karyawan())
    
    while True:
        print("\nPilih opsi:")
        print("1. Cari berdasarkan NIP")
        print("2. Cari berdasarkan Nama")
        print("3. Cari berdasarkan Alamat")
        print("4. Cari berdasarkan Departemen")
        print("5. Cari berdasarkan Jabatan")
        print("6. Tampilkan semua data karyawan")
        print("7. Keluar")
        
        pilihan = input("Masukkan pilihan (1-7): ")

        if pilihan == '1':
            nip = input("Masukkan NIP yang ingin dicari: ")
            cari_karyawan(karyawan_list, 'NIP', nip)
        elif pilihan == '2':
            nama = input("Masukkan Nama yang ingin dicari: ")
            cari_karyawan(karyawan_list, 'Nama', nama)
        elif pilihan == '3':
            alamat = input("Masukkan Alamat yang ingin dicari: ")
            cari_karyawan(karyawan_list, 'Alamat', alamat)
        elif pilihan == '4':
            departemen = input("Masukkan Departemen yang ingin dicari: ")
            cari_karyawan(karyawan_list, 'Departemen', departemen)
        elif pilihan == '5':
            jabatan = input("Masukkan Jabatan yang ingin dicari: ")
            cari_karyawan(karyawan_list, 'Jabatan', jabatan)
        elif pilihan == '6':
            tampilkan_karyawan(karyawan_list)
        elif pilihan == '7':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 7.")

if __name__ == "__main__":
    main()

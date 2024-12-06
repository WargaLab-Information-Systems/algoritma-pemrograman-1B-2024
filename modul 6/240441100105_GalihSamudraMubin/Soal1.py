daftar_karyawan = []

def tambah_karyawan():
    print("\n--- Tambah Data Karyawan ---")
    while len(daftar_karyawan) < 5:
        nip = input("Masukkan NIP: ")
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        departemen = input("Masukkan Departemen: ")
        jabatan = input("Masukkan Jabatan: ")

        karyawan = (nip, nama, alamat, departemen, jabatan)
        daftar_karyawan.append(karyawan)
        print(f"Data karyawan berhasil ditambahkan. Total karyawan: {len(daftar_karyawan)}/5\n")
    
    print("Data karyawan minimal (5) telah terpenuhi.\n")

def lihat_karyawan():
    if len(daftar_karyawan) < 5:
        print("\nBelum cukup data karyawan (minimal 5) untuk ditampilkan.")
        return
    
    print("\n--- Daftar Karyawan ---")
    for karyawan in daftar_karyawan:
        print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def cari_karyawan():
    if len(daftar_karyawan) < 5:
        print("\nBelum cukup data karyawan (minimal 5) untuk pencarian.")
        return

    atribut = input("\nCari berdasarkan (nip/nama/alamat/departemen/jabatan): ").lower()
    nilai = input("Masukkan Kata Kunci yang ingin dicari: ").lower()

    print(f"\n--- Hasil Pencarian Berdasarkan {atribut.capitalize()} ---")
    ditemukan = False

    for karyawan in daftar_karyawan:
        if (
            (atribut == "nip" and karyawan[0].lower() == nilai) or
            (atribut == "nama" and karyawan[1].lower() == nilai) or
            (atribut == "alamat" and karyawan[2].lower() == nilai) or
            (atribut == "departemen" and karyawan[3].lower() == nilai) or
            (atribut == "jabatan" and karyawan[4].lower() == nilai)
        ):
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
            ditemukan = True

    if not ditemukan:
        print("Data karyawan tidak ditemukan.")

def main():
    while len(daftar_karyawan) < 5:
        tambah_karyawan()
    
    while True:
        print("\nMenu Sistem Manajemen Karyawan")
        print("1. Tambah Karyawan")
        print("2. Lihat Semua Karyawan")
        print("3. Cari Karyawan")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_karyawan()
        elif pilihan == "2":
            lihat_karyawan()
        elif pilihan == "3":
            cari_karyawan()
        elif pilihan == "4":
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

main()
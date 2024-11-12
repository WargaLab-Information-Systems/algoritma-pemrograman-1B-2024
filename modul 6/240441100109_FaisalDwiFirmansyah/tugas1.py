data_karyawan = []
def tambah_karyawan():
    nip = input("\nMasukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")

    karyawan_baru = (nip, nama, alamat, departemen, jabatan)
    data_karyawan.append(karyawan_baru)
    print("\nData karyawan berhasil ditambahkan!")

def tampilkan_karyawan(karyawan):
    print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def cari_karyawan(atribut, nilai):
    hasil_cari = [karyawan for karyawan in data_karyawan if karyawan[atribut] == nilai]
    if hasil_cari:
        print("\nData karyawan yang ditemukan:")
        for karyawan in hasil_cari:
            tampilkan_karyawan(karyawan)
    else:
        print("\nTidak ada karyawan yang sesuai dengan pencarian.")

def main():
    print("=== Pencarian Data Karyawan ===")
    
    while True:
        tambah_karyawan()
        lanjut = input("Apakah Anda ingin menambahkan karyawan lagi? (Y/N): ")
        if lanjut != 'y' :
            break

    # Menu utama
    while True:
        print("\nPilih pencarian berdasarkan:")
        print("1. NIP")
        print("2. Nama")
        print("3. Alamat")
        print("4. Departemen")
        print("5. Jabatan")
        print("6. Tampilkan Semua Data")
        print("7. Keluar")

        pilihan = input("Masukkan pilihan (1-7): ")

        if pilihan == "1":
            nilai = input("Masukkan NIP yang dicari: ")
            cari_karyawan(0, nilai)
        elif pilihan == "2":
            nilai = input("Masukkan Nama yang dicari: ")
            cari_karyawan(1, nilai)
        elif pilihan == "3":
            nilai = input("Masukkan Alamat yang dicari: ")
            cari_karyawan(2, nilai)
        elif pilihan == "4":
            nilai = input("Masukkan Departemen yang dicari: ")
            cari_karyawan(3, nilai)
        elif pilihan == "5":
            nilai = input("Masukkan Jabatan yang dicari: ")
            cari_karyawan(4, nilai)
        elif pilihan == "6":
            print("\nData Seluruh Karyawan:")
            for karyawan in data_karyawan:
                tampilkan_karyawan(karyawan)
        elif pilihan == "7":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
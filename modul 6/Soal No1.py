# Program Pendataan Karyawan 
karyawan_list = []        

# Fungsi untuk menambahkan data karyawan
def tambah_karyawan():
    karyawan = {
        "NIP": input("Masukkan NIP: "),
        "Nama": input("Masukkan Nama: "),
        "Alamat": input("Masukkan Alamat: "),
        "Departemen": input("Masukkan Departemen: "),
        "Jabatan": input("Masukkan Jabatan: ")
    }
    karyawan_list.append(karyawan) 
    print("Data karyawan berhasil ditambahkan!\n")

# Fungsi untuk mencari karyawan berdasarkan atribut tertentu
def cari_karyawan():
    kriteria = input("Cari berdasarkan (NIP/Nama/Alamat/Departemen/Jabatan): ")
    nilai_cari = input(f"Masukkan {kriteria} yang dicari: ")

    hasil_cari = [karyawan for karyawan in karyawan_list if karyawan[kriteria] == nilai_cari]   
    
    if hasil_cari:
        print("\nData karyawan yang sesuai:")
        for karyawan in hasil_cari:
            print(f"NIP       : {karyawan['NIP']}")
            print(f"Nama      : {karyawan['Nama']}")
            print(f"Alamat    : {karyawan['Alamat']}")
            print(f"Departemen: {karyawan['Departemen']}")
            print(f"Jabatan   : {karyawan['Jabatan']}\n")
    else:
        print("Data karyawan tidak ditemukan.\n")

# Fungsi utama
def main():
    print("=== Program Pendataan Karyawan Sederhana ===")
    
    # Masukkan minimal 5 data karyawan
    for i in range(5):
        print(f"\nMasukkan data karyawan ke-{i+1}:") #digunakan agar tampilan angka mulai dari 1 hingga 5 
        tambah_karyawan()

    while True:
        pilihan = input("\nPilih menu (1: Tambah, 2: Cari, 3: Lihat Semua, 4: Keluar): ")

        if pilihan == "1":
            tambah_karyawan()
        elif pilihan == "2":
            cari_karyawan()
        elif pilihan == "3":
            print("\nSeluruh data karyawan:")
            for karyawan in karyawan_list:
                print(f"NIP       : {karyawan['NIP']}")
                print(f"Nama      : {karyawan['Nama']}")
                print(f"Alamat    : {karyawan['Alamat']}")
                print(f"Departemen: {karyawan['Departemen']}")
                print(f"Jabatan   : {karyawan['Jabatan']}\n")
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

main()
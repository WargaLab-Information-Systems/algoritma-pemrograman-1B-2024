siswa = []
nama_siswa = set()

def tambahkan_data():
    nama = input("Masukkan Nama Siswa : ")

    if nama in nama_siswa:
        print(f"Siswa dengan nama {nama} sudah ada. Silahkan masukkan nama atau karakter yang berbeda.")
        return
    
    assek = input("Masukkan Asal Sekolah : ")
    plot = input("Masukkan Plotting Bimbingan : ")

    siswa_baru = {"nama": nama,
                   "asal sekolah" : assek,
                   "plotting" : plot}
    siswa.append(siswa_baru)
    nama_siswa.add(nama)
    print(f"Siswa atas nama {nama} berhasil ditambahkan.\n")

def tampilkan_data():
    if siswa :
        print("Daftar Siswa Ditampilkan : ")
        for data in siswa :
            print(f"Nama: {data["nama"]}, Asal Sekolah : {data["asal sekolah"]}, Plotting Bimbingan : {data["plotting"]}")
    else:
        print("Belum ada data siswa.")

def kelompok_siswa():
    kelas = {}
    for siswa_data in siswa:
        nomor_kelas = (siswa.index(siswa_data) // 3) + 1
        nama_kelas = f"Kelas {nomor_kelas}"
        if nama_kelas not in kelas:
            kelas[nama_kelas] = []
        kelas[nama_kelas].append(siswa_data)

    print("\nPengelompokan Siswa per Kelas:")
    for nama_kelas, siswa_list in kelas.items():
        print(f"\n{nama_kelas}:")
        for data in siswa_list:
            print(f" ~ Nama: {data["nama"]}, Asal Sekolah: {data["asal sekolah"]}, Plotting: {data["plotting"]}")

def ubah_data():
    if siswa:
        tampilkan_data()
        nama = input("Nama siswa yang datanya ingin diubah: ")
        for data in siswa:
            if data["nama"] == nama:
                print(f"Data sebelum diubah: Nama: {data['nama']}, Asal Sekolah: {data['asal sekolah']}, Plotting Bimbingan: {data['plotting']}\n")

                # Memperbarui data siswa
                data["nama"] = input("Masukkan nama baru : ") or data["nama"]
                data["asal sekolah"] = input("Masukkan asal sekolah baru : ") or data["asal sekolah"]
                data["plotting"] = input("Masukkan plotting bimbingan yang baru : ") or data["plotting"]
                
                # Mengelola nama dalam set
                nama_siswa.discard(nama)  
                nama_siswa.add(data["nama"]) 
                
                print("Data siswa berhasil diubah.")
                return
        print("Siswa dengan nama tersebut tidak ditemukan.")
    else:
        print("Belum ada data siswa.")


def hapus_data():
    if siswa:
        tampilkan_data()
        nama_hapus = input("Nama siswa yang ingin dihapus: ")
        
        # Mencari dan menghapus data berdasarkan nama
        for data in siswa:
            if data["nama"] == nama_hapus:
                siswa.remove(data)
                nama_siswa.discard(nama_hapus)
                print(f"Data siswa dengan nama {nama_hapus} berhasil dihapus.")
                return
        print("Nama siswa tidak ditemukan.")
    else:
        print("Belum ada data siswa.")


while True :
    menu = input('''
            Lembaga Bimbingan Intensif Gema Ripah
                 
                 1. Menambahkan Data Siswa
                 2. Menampilkan Data Siswa
                 3. Mengelompokkan Siswa Berdasarkan Data
                 4. Mengubah Data Siswa
                 5. Menghapus Data Siswa
                 6. Keluar dari Program
                 
            Masukkan Menu Berdasarkan Kebutuhan (1-5) : ''')
    
    if menu == "1":
        tambahkan_data()
    elif menu == "2":
        tampilkan_data()
    elif menu == "3":
        kelompok_siswa()
    elif menu == "4":
        ubah_data()
    elif menu == "5":
        hapus_data()
    elif menu == "6":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan anda salah.")
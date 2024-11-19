siswa = []

def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    sekolah = input("Masukkan asal sekolah: ")
    plotting = input("Masukkan plotting siswa: ")

    siswa_baru = {"nama": nama, "sekolah": sekolah, "plotting": plotting}
    siswa.append(siswa_baru)
    print(f"***Siswa {nama} berhasil ditambahkan***")

def tampilkan_siswa():
    if len(siswa) == 0:
        print("Belum ada data siswa yang bisa ditampilkan")
        return
    print("***Daftar Siswa***")
    for i in range(len(siswa)):
        print(f"{i + 1}. Nama: {siswa[i]['nama']}, Sekolah: {siswa[i]['sekolah']}, Plotting: {siswa[i]["plotting"]}")
        
def ubah_siswa():
    if len(siswa) == 0:
        print("Belum ada data siswa yang bisa diubah")
        return
    tampilkan_siswa()
    nomor_siswa = int(input("Nomor data siswa yang ingin diubah: ")) - 1
    if 0 <= nomor_siswa < len(siswa):
        siswa_data = siswa[nomor_siswa]
     
        nama_baru = input(f"Nama ({siswa_data['nama']}): ")
        if nama_baru != "":
            siswa_data['nama'] = nama_baru
        
        sekolah_baru = input(f"Sekolah ({siswa_data['sekolah']}): ")
        if sekolah_baru != "":
            siswa_data['sekolah'] = sekolah_baru

        plotting_baru = input(f"Kelas ({siswa_data['plotting']}): ")
        if plotting_baru != "":
            siswa_data['plotting'] = plotting_baru
        
        print("***Data siswa berhasil diubah!***")
    else:
        print("Siswa tidak ditemukan!!!")

def hapus_siswa():
    if len(siswa) == 0:
        print("Belum ada data siswa untuk dihapus")
        return
    tampilkan_siswa()
    nomor_siswa = int(input("Nomor siswa yang ingin dihapus: ")) - 1
    if 0 <= nomor_siswa < len(siswa):
        siswa_dihapus = siswa.pop(nomor_siswa)
        print(f"***Siswa {siswa_dihapus['nama']} berhasil dihapus!***")
    else:
        print("Siswa tidak ditemukan.")

def kelompokkan_siswa():
    kelas = {}
    for i in range(len(siswa)):
        nomor_kelas = i // 3 + 1
        nama_kelas = f"***Kelas {nomor_kelas}***"

        if nama_kelas not in kelas:  
            kelas[nama_kelas] = []

        kelas[nama_kelas].append(siswa[i]) 
    
    print("Pengelompokan Siswa per Kelas:")
    for nama_kelas, siswa_list in kelas.items():
        print (f"{nama_kelas}:")
        for siswa_data in siswa_list:
            print(f" - {siswa_data['nama']} (Sekolah: {siswa_data['sekolah']}, Plotting: {siswa_data['plotting']})")

def menu():
    while True:
        print("*** MENU ***")
        print("1. Tambah Siswa")
        print("2. Lihat Daftar Siswa")
        print("3. Ubah Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Kelompokkan Siswa per Kelas")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            tambah_siswa()
        elif pilihan == '2':
            tampilkan_siswa()
        elif pilihan == '3':
            ubah_siswa()
        elif pilihan == '4':
            hapus_siswa()
        elif pilihan == '5':
            kelompokkan_siswa()
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()
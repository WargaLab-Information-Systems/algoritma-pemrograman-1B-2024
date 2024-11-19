siswa_data = []  
kelas_data = {}  

def update_kelas(): 
    kelas_data.clear()
    for i in range(len(siswa_data)):
        kelas_no = i // 3 + 1 
        kelas_key = f"Kelas {kelas_no}"
        if kelas_key not in kelas_data:
            kelas_data[kelas_key] = []
        kelas_data[kelas_key].append(siswa_data[i])

def tambah_siswa(): 
    nama = input("Masukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah: ")
    plotting = input("Masukkan plotting bimbingan: ")
    siswa_data.append({"nama": nama, "asal_sekolah": asal_sekolah, "plotting": plotting})
    update_kelas()
    print(f"Siswa '{nama}' berhasil ditambahkan ke data!\n")

def lihat_siswa():
    if not siswa_data:
        print("Belum ada data siswa.\n")
    else:
        print("Data Siswa:")
        for i, siswa in enumerate(siswa_data):
            print(f"{i + 1}. Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}, Plotting: {siswa['plotting']}")
        print()

def hapus_siswa():
    lihat_siswa()
    if not siswa_data:
        return 

    index = int(input("Masukkan nomor siswa yang ingin dihapus: "))
    if 1 <= index <= len(siswa_data): 
        siswa = siswa_data.pop(index - 1)
        update_kelas()
        print(f"Siswa '{siswa['nama']}' berhasil dihapus dari data!\n")
    else:
        print("Nomor siswa tidak valid.\n")

def update_siswa():
    lihat_siswa()
    if not siswa_data:
        return  
    index = int(input("Masukkan nomor siswa yang ingin diupdate: "))
    if 1 <= index <= len(siswa_data):
        siswa = siswa_data[index - 1]
        print(f"Data lama: Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}, Plotting: {siswa['plotting']}")
        
        nama_baru = input("Masukkan nama baru : ")
        asal_sekolah_baru = input("Masukkan asal sekolah baru : ")
        plotting_baru = input("Masukkan plotting baru : ")

        if nama_baru:
            siswa['nama'] = nama_baru
        if asal_sekolah_baru:
            siswa['asal_sekolah'] = asal_sekolah_baru
        if plotting_baru:
            siswa['plotting'] = plotting_baru

        update_kelas()
        print(f"Data siswa nomor {index} berhasil diperbarui!\n")
    else:
        print("Nomor siswa tidak valid.\n")

def lihat_kelas():
    """Melihat pembagian kelas berdasarkan data siswa."""
    if not kelas_data:
        print("Belum ada kelas yang tersedia.\n")
    else:
        print("Pembagian Kelas:")
        for kelas, siswa_list in kelas_data.items():
            print(f"{kelas}:")
            for siswa in siswa_list:
                print(f"  - {siswa['nama']} (Asal Sekolah: {siswa['asal_sekolah']}, Plotting: {siswa['plotting']})")
        print()

while True:
    print("Menu:")
    print("1. Tambah Siswa")
    print("2. Lihat Siswa")
    print("3. Hapus Siswa")
    print("4. Lihat Pembagian Kelas")
    print("5. Update Siswa")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        lihat_siswa()
    elif pilihan == "3":
        hapus_siswa()
    elif pilihan == "4":
        lihat_kelas()
    elif pilihan == "5":
        update_siswa()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.\n")

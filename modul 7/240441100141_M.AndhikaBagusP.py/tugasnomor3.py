def tambahkan_data(nama, asalSekolah):
    siswa = {
        'nama' : nama,
        'asal sekolah' : asalSekolah,
    }
    dataSiswa.append(siswa)
    print(f"Data siswa bernama {nama} berhasil ditambahkan")
    
def penentuan_kelas(dataSiswa):
    kelas = []
    for i in range (len(dataSiswa)):
        if i % 3 == 0:
            kelas.append([])
        kelas[-1].append(dataSiswa[i])
                         
    return kelas
    
def tampilkan_data(dataSiswa):
    if not dataSiswa:
        print("Tidak ada data siswa")
    
    kelas = penentuan_kelas(dataSiswa)
    for i in range (len(kelas)):
        print(f"== Kelas {i+1}==")
        for siswa in kelas[i]:
            print(f"Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal sekolah']} ")
        
def hapus_data(dataSiswa):
    pilihanHapus = input("Masukkan nama siswa yang ingin dihapus: ").lower()
    for siswa in dataSiswa:
        if siswa['nama'] == pilihanHapus:
            dataSiswa.remove(siswa)
            print("Data siswa telah dihapus")
            return 
    print("Data siswa tidak ditemukan")
    
def update_data(dataSiswa):
    pilihanUpdate = input("Masukkan nama siswa yang ingin di update: ").lower()
    for siswa in dataSiswa:
        if siswa['nama'] == pilihanUpdate:
            namaBaru = input("Masukkan nama siswa yang baru: ").lower()
            asalSekolahBaru = input("Masukkan asal sekolah baru: ").lower()
            siswa['nama'] = namaBaru
            siswa['asal sekolah'] = asalSekolahBaru
            print("Data siswa telah diupdate")
            return
    print("Data tidak ditemukan")        
    
dataSiswa = []

while True:
    print("=======Menu=======")
    print("1. Tambahkan data")
    print("2. Tampilkan data")
    print("3. Update data")
    print("4. Hapus data")
    print("0. Keluar")
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == "1":
        nama = input("Masukkan nama: ").lower()
        asalSekolah = input("Masukkan asal sekolah: ").lower()
        tambahkan_data(nama, asalSekolah)
        
    elif pilihan == "2":
        tampilkan_data(dataSiswa)
        
    
    elif pilihan == "3":
        update_data(dataSiswa)
    
    elif pilihan == "4":
        hapus_data(dataSiswa)
    
    elif pilihan == "0":
        break
    
    else:
        print("Pilihan tidak sesuai")
# Dictionary untuk menyimpan data siswa
data_siswa = {}

def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah: ")
    plotting = input("Masukkan plotting bimbingan: ")
    # Hitung jumlah kelas yang ada
    kelas_terakhir = len(data_siswa)
    
    # Jika belum ada kelas atau kelas terakhir sudah penuh (3 siswa)
    if kelas_terakhir == 0 or len(data_siswa[f"Kelas {kelas_terakhir}"]) == 3:
        kelas_terakhir += 1
        # Buat kelas baru
        data_siswa[f"Kelas {kelas_terakhir}"] = []
    
    # Tambahkan siswa ke kelas terakhir
    data_siswa[f"Kelas {kelas_terakhir}"].append({
        "nama": nama,
        "asal_sekolah": asal_sekolah,
        "plotting": plotting
    })
    print(f"{nama} berhasil ditambahkan ke Kelas {kelas_terakhir}.")

def tampilkan_data():
    if not data_siswa:
        print("Tidak ada data siswa.")
    else:
        for kelas, siswa in data_siswa.items():
            print(f"\n{kelas}:")
            for d, data in enumerate(siswa, start=1):
                print(f"{d}. Nama: {data['nama']}, Asal Sekolah: {data['asal_sekolah']}, Plotting: {data['plotting']}")

def ubah_data():
    nama_lama = input("Masukkan nama siswa yang ingin diubah: ")
    for kelas, siswa in data_siswa.items():
        for data in siswa:
            if data["nama"] == nama_lama:
                print("Masukkan data baru:")
                data["nama"] = input("Masukkan nama baru: ")
                data["asal_sekolah"] = input("Masukkan asal sekolah baru: ")
                data["plotting"] = input("Masukkan plotting baru: ")
                print("Data berhasil diubah.")
                return
    print("Data siswa tidak ditemukan.")

def hapus_data():
    nama = input("Masukkan nama siswa yang ingin dihapus: ")
    for kelas, siswa in data_siswa.items():
        for data in siswa:
            if data["nama"] == nama:
                # Hapus data siswa dari kelas
                siswa.remove(data)
                print("Data berhasil dihapus.")
                
                # Jika kelas kosong setelah penghapusan, hapus kelas tersebut
                if not siswa:
                    del data_siswa[kelas]
                return
    print("Data siswa tidak ditemukan.")

# Menu utama
while True:
    print("\nMenu:")
    print("1. Tambah siswa")
    print("2. Tampilkan data siswa")
    print("3. Ubah data siswa")
    print("4. Hapus data siswa")
    print("5. Keluar")
    pilihan = input("\nPilih menu: ")
    
    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        print("Keluar dari program. Terima kasih.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
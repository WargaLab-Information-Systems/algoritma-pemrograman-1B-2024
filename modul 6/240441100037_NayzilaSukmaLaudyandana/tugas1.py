nips = []
names = []
addresses = []
departments = []
positions = []

def tambah_karyawan():
    for i in range(5): 
        print(f"\nMasukkan data karyawan ke-{i+1}")
        nips.append(input("NIP: "))
        names.append(input("Nama: "))
        addresses.append(input("Alamat: "))
        departments.append(input("Departemen: "))
        positions.append(input("Jabatan: "))
    
    print("\nData karyawan berhasil ditambahkan!\n")

def tampilkan_semua_karyawan():
    print("\nSeluruh Data Karyawan:")
    for i in range(len(nips)):
        print(f"NIP: {nips[i]}, Nama: {names[i]}, Alamat: {addresses[i]}, Departemen: {departments[i]}, Jabatan: {positions[i]}")
    print()

def cari_karyawan():
    print("\nPilih kriteria pencarian:")
    print("1. NIP\n2. Nama\n3. Alamat\n4. Departemen\n5. Jabatan")
    pilihan = int(input("Masukkan nomor kriteria pencarian (1-5): "))
    nilai_cari = input("Masukkan nilai yang dicari: ")
    print("\nHasil Pencarian:")
    ditemukan = False

    for i in range(len(nips)):
        if (pilihan == 1 and nips[i] == nilai_cari) or \
           (pilihan == 2 and names[i] == nilai_cari) or \
           (pilihan == 3 and addresses[i] == nilai_cari) or \
           (pilihan == 4 and departments[i] == nilai_cari) or \
           (pilihan == 5 and positions[i] == nilai_cari):
            print(f"NIP: {nips[i]}, Nama: {names[i]}, Alamat: {addresses[i]}, Departemen: {departments[i]}, Jabatan: {positions[i]}")
            ditemukan = True

    if not ditemukan:
        print("Data karyawan tidak ditemukan sesuai kriteria yang dicari.")

tambah_karyawan()  
tampilkan_semua_karyawan() 

while True:
    cari_karyawan()
    ulang = input("Apakah ingin mencari lagi? (y/n): ").lower()
    if ulang != 'y':
        break

print("Program selesai.")

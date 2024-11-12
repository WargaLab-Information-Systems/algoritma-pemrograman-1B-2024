data = []
def data_karyawan():
    for i in range(5):
        print(f"masukan data karyawab ke-{i+1}")
        nip = input("Masukan NIP:")
        nama = input("Maasukan nama: ")
        alamat = input("Masukan alamat: ")
        departemen = input("Masukan departemen: ")
        jabatan = input("Masukan jabatan: ")
        karyawan = (nip, nama, alamat, departemen, jabatan)
        data.append(karyawan)
        print("Data berhasil ditambahkan.")

def cari_karyawan():
    while True:
        print("\nMenu Pencarian: ")
        print("1. Cari berdasarkan NIP: ")
        print("2. Cari berdasarkan nama: ")
        print("3. Cari berdasarkan alamat: ")
        print("4. Cari berdasarkan departemen: ")
        print("5. Cari berdasarkan jabatan: ")
        print("6. Keluar")
        opsi = input("Masukan opsi yang ingin dicari (nip/nama/alamat/departemen/jabatan): ")
        hasil = input("Masukan hasil pencarian: ")

        if opsi == "nip":
            artibut = 0
        elif opsi == "nama":
            artibut = 1
        elif opsi == "alamat":
            artibut = 2
        elif opsi == "departemen":
            artibut = 3
        elif opsi == "jabatan":
            artibut = 4
        else:
            print("Pilihan tidak valid.")
        
        hasil_pencarian = []
        for karyawan in data:
            if karyawan[artibut] == hasil:
                hasil_pencarian.append(karyawan)

        if hasil:
            print("\nHasil pencarian: ")
            for karyawan in hasil_pencarian:
                print(f"NIP: {karyawan[0]}, nama: {karyawan[1]}, alamat: {karyawan[2]}, departemen {karyawan[3]}, jabatan {karyawan[4]}")
        else: 
            print("Data tidak ditemukan")
        break 

data_karyawan()
cari_karyawan()
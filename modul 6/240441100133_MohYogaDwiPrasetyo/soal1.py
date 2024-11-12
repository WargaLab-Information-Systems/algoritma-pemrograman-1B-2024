karyawan_list = []

def tambah_karyawan():
    for i in range(5):
        print(f"\nData karyawan ke-{i+1}")
        nip = input("Masukkan NIP: ")
        nama = input("Masukkan nama: ")
        alamat = input("Masukkan alamat: ")
        departemen = input("Masukkan departemen: ")
        jabatan = input("Masukkan jabatan: ")
        
        # nyimpen data karyawan sebagai list
        karyawan = [nip, nama, alamat, departemen, jabatan]
        karyawan_list.append(karyawan)
        print("Data karyawan berhasil ditambahkan.")

def cari_karyawan():
    atribut = input("Masukkan atribut pencarian (nip/nama/alamat/departemen/jabatan): ")
    if atribut not in ["nip", "nama", "alamat", "departemen", "jabatan"]:
        print("Atribut tidak valid!!!")
        return
    nilai = input(f"Masukkan {atribut} yang ingin dicari: ")
    indeks = ["nip", "nama", "alamat", "departemen", "jabatan"].index(atribut) 
    hasil = [k for k in karyawan_list if k[indeks] == nilai] 
    
    if hasil:
        for data in hasil:
            data_karyawan = (f"['NIP': '{data[0]}', 'Nama': '{data[1]}', 'Alamat': '{data[2]}', 'Departemen': '{data[3]}', 'Jabatan': '{data[4]}']")
            print(data_karyawan)
    else:
        print("Data tidak ditemukan.")

def tampilkan_karyawan():
    if karyawan_list:
        for karyawan in karyawan_list:
            data_karyawan = f"['NIP': '{karyawan[0]}', 'Nama': '{karyawan[1]}', 'Alamat': '{karyawan[2]}', 'Departemen': '{karyawan[3]}', 'Jabatan': '{karyawan[4]}']"
            print(data_karyawan)
    else:
        print("Belum ada data karyawan.")

tambah_karyawan()

while True:
    print("\nMenu: ")
    print("1. Cari karyawan")
    print("2. Tampilkan semua karyawan")
    print("3. Keluar")
    
    pilihan = int(input("\nPilih (1/2/3): "))
    if pilihan == 1:
        cari_karyawan()
    elif pilihan == 2:
        tampilkan_karyawan()
    elif pilihan == 3:
        print("Terimakasih...")
        break
    else:
        print("Pilihan tidak valid!")
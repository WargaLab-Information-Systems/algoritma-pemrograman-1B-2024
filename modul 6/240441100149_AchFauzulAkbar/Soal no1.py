list_data_karyawan = []

def input_karyawan(nip, nama, alamat, departemen, jabatan):
    karyawan = (nip, nama, alamat, departemen, jabatan)
    list_data_karyawan.append(karyawan)

def cari_hasil(list_data_karyawan, atribut, nilai):
    hasil_cari = []
    for karyawan in list_data_karyawan:
        if karyawan[atribut] == nilai:  # Mengakses atribut dengan indeks
            hasil_cari.append(karyawan)
    return hasil_cari

def tampilkan_karyawan(list_data_karyawan):
    for karyawan in list_data_karyawan:
        print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def menu_data():
    while True:
        print('Menu:')
        print('1. Input Data')
        print('2. Cari Data')
        print('3. Tampilkan Data')
        print('4. Keluar')

        menu_input = input('Pilih menu: ')
        
        if menu_input == '1':
            for i in range(5):  # Loop untuk input lima data
                nip = int(input(f'Masukkan NIP karyawan ke-{i+1}: '))
                nama = input(f'Masukkan Nama karyawan ke-{i+1}: ')
                alamat = input(f'Masukkan Alamat karyawan ke-{i+1}: ')
                departemen = input(f'Masukkan Departemen karyawan ke-{i+1}: ')
                jabatan = input(f'Masukkan Jabatan karyawan ke-{i+1}: ')
                input_karyawan(nip, nama, alamat, departemen, jabatan)

        elif menu_input == '2':
            atribut = int(input('Pilih atribut untuk mencari (0: NIP, 1: Nama, 2: Alamat, 3: Departemen, 4: Jabatan): '))
            nilai = input('Masukkan nilai yang dicari: ')
            # Jika atribut adalah NIP, konversi nilai ke integer untuk perbandingan
            if atribut == 0:
                nilai = int(nilai)
            hasil = cari_hasil(list_data_karyawan, atribut, nilai)
            if hasil:
                print("Data ditemukan:")
                tampilkan_karyawan(hasil)
            else:
                print("Data tidak ditemukan.")

        elif menu_input == '3':
            tampilkan_karyawan(list_data_karyawan)

        elif menu_input == '4':
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu_data()
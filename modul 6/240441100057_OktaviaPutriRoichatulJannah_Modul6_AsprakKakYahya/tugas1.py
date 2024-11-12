daftar_karyawan = []

def input_data_karyawan():
    
    print("***Masukkan data karyawan***")
    print()
    for i in range(5):
        print(f"------Masukkan data karyawan ke-{i+1}------")
        NIP = input("Masukkan NIP karyawan: ")
        Nama = input("Masukkan Nama karyawan: ")
        Alamat = input("Masukkan Alamat karyawan: ")
        Departemen = input("Masukkan Departemen karyawan: ")
        Jabatan = input("Masukkan Jabatan karyawan: ")

        karyawan_baru = (NIP,Nama,Alamat,Departemen,Jabatan)
        daftar_karyawan.append(karyawan_baru)

    while True:
        tambah_data = input("Apakah anda ingin menambah data karyawan lagi(y/n): ")

        if tambah_data == "y":
            NIP = input("Masukkan NIP karyawan: ")
            Nama = input("Masukkan Nama karyawan: ")
            Alamat = input("Masukkan Alamat karyawan: ")
            Departemen = input("Masukkan Departemen karyawan: ")
            Jabatan = input("Masukkan Jabatan karyawan: ")

            karyawan_baru = (NIP,Nama,Alamat,Departemen,Jabatan)
            daftar_karyawan.append(karyawan_baru)
        
        elif tambah_data == "n":
            break
        else:
            print("Input tidak valid!!! silahkan masukkan y atau n ")

def tampilkan_karyawan(karyawan):
    print(f"NIP: {karyawan[0]},Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def cari_karyawan(atribut,nilai):

    hasil_cari = [karyawan for karyawan in daftar_karyawan if karyawan[atribut] == nilai]
    if hasil_cari:
        print()
        print("===Data karyawan ditemukan sebagai berikut===")
        print()
        for karyawan in hasil_cari:
            tampilkan_karyawan(karyawan)
    else:
        print("===Tidak ada karyawan yang sesuai dengan data tersebut===")


def main():

    daftar_karyawan = input_data_karyawan()

    while True:
        print()
        print("========Pencarian Karyawan========")
        print("1. Cari berdasarkan NIP")
        print("2. Cari berdasarkan Nama")
        print("3. Cari berdasarkan Alamat")
        print("4. Cari berdasarkan Departemen")
        print("5. Cari berdasarkan Jabatan")
        print("6. Keluar")
        
        pilihan = input("Pilih fitur pencarian (1-6): ")

        if pilihan == '1':
            nilai = input("Masukkan NIP yang dicari: ")
            cari_karyawan(0,nilai)
        elif pilihan == '2':
            nilai = input("Masukkan Nama yang dicari: ")
            cari_karyawan(1,nilai)
        elif pilihan == '3':
            nilai = input("Masukkan Alamat yang dicari: ")
            cari_karyawan(2,nilai)
        elif pilihan == '4':
            nilai = input("Masukkan Departemen yang dicari: ")
            cari_karyawan(3,nilai)
        elif pilihan == '5':
            nilai = input("Masukkan Jabatan yang dicari: ")
            cari_karyawan(4,nilai)
        elif pilihan == '6':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
            continue

main()

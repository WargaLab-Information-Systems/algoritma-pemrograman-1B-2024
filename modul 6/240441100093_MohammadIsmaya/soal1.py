
daftar_karyawan = []

# Fungsi tambah karyawan
def tambah_karyawan(nip, nama, alamat, departemen, jabatan):
    karyawan_baru = [nip, nama, alamat, departemen, jabatan]
    daftar_karyawan.append(karyawan_baru)

    return karyawan_baru
    
# Fungsi mencari karyawan
def cari_karyawan(opsi, kata_kunci):
    opsi = int(opsi) 
    hasil = [] 

    if not daftar_karyawan: 
        return hasil 

    for karyawan in daftar_karyawan:
        if kata_kunci in karyawan[opsi]:
            hasil.append(karyawan) 
    
    return hasil

# Fungsi menjalankan tambah secara berulang
def tambah_ulang(banyak_ulang):
    daftar_penambahan = []

    if banyak_ulang < 5:
        return daftar_penambahan

    for i in range(banyak_ulang):
        nip = input("Masukkan NIP karyawan: ")
        nama = input("Masukkan nama karyawan: ")
        alamat = input("alamat:")
        departemen = input("Masukkan departemen karyawan: ")
        jabatan = input("Masukkan jabatan karyawan:")

        hasil_tambah = tambah_karyawan(nip, nama, alamat, departemen, jabatan)
        daftar_penambahan.append(hasil_tambah)
    
    return daftar_penambahan

# Program utama
while True:
    print("Menu:")
    print("1. Tambah karyawan\n2. Cari karyawan\n0. Keluar")
    menu = input("Masukkan pilihan anda: ")

    # Tambah karyawan
    if menu == "1":
        banyak_tambah = int(input("\nBerapa banyak karyawan yang ingin ditambahkan?: "))
        hasil = tambah_ulang(banyak_tambah)

        if not hasil:
            print("Jumlah minimal penambahan karyawan adalah 5!\n")
            continue

        print("Penambahan karyawan berhasil!")
        print(f"List karyawan yang telah ditambahkan:\n{hasil}\n")

    # Cari karyawan
    elif menu == "2":
        list_opsi = ["NIP", "Nama", "Alamat", "Departemen", "Jabatan"]
        
        print("\nIngin mencari karyawan berdasarkan apa?:")
        for opsi in range(len(list_opsi)):
            print(f"{opsi}. {list_opsi[opsi]}") #menggabungkan nomer urut dengan nama opsi
        
        opsi = input("Masukkan opsi anda: ")
        kata_kunci = input("Masukkan kata kunci: ")

        hasil = cari_karyawan(opsi, kata_kunci)

        print("Hasil pencarian:")
        
        if not hasil:
           print("Data tidak ditemukan!\n")
           continue
        
        for data in hasil:
            for i in range(len(data)):
                print(f"{list_opsi[i]}\t\t: {data[i]}")
        
        print()

    # Keluar program
    elif menu == "0":
        print("Program diakhiri")
        break

    # Opsi yang tidak tersedia
    else:
        print("Maaf menu yang anda pilih tidak tersedia dalam menu!\n")
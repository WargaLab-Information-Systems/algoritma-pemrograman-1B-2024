def tambah_barang(barang_list):
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    print("Pilih Tingkat Prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    prioritas = input("Pilih (1/2/3): ")


    if prioritas == '1':
        prioritas_numerik = 1

    elif prioritas == '2':
        prioritas_numerik = 2
    
    elif prioritas == '3':
        prioritas_numerik = 3
    
    else:
        print("Prioritas tidak valid!")
        return barang_list


    barang_list.append((nama_barang, id_barang, prioritas_numerik))


    darurat = []
    biasa = []
    non_darurat = []

    for barang in barang_list:
        if barang[2] == 1:
            darurat.append(barang)
        
        elif barang[2] == 2:
            biasa.append(barang)
        
        elif barang[2] == 3:
            non_darurat.append(barang)


    barang_list = darurat + biasa + non_darurat

    print("Barang berhasil ditambahkan!")
    return barang_list

def tampilkan_barang(barang_list):
    if not barang_list:
        print("Belum ada data barang.")
    else:
        print("Daftar Barang:")
        for barang in barang_list:

            if barang[2] == 1:
                prioritas_str = "Darurat"
            
            elif barang[2] == 2:
                prioritas_str = "Biasa"
            
            elif barang[2] == 3:
                prioritas_str = "Non-Darurat"
            

            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {prioritas_str}")

def main():
    barang_list = []

    while True:
        print("Pengelola Pengiriman Barang")
        print("1. Tambah Barang")
        print("2. Tampilkan Daftar Barang")
        print("3. Keluar")

        pilihan = input("menu (1/2/3): ")

        if pilihan == '1':
            barang_list = tambah_barang(barang_list)
        
        elif pilihan == '2':
            tampilkan_barang(barang_list)
        
        elif pilihan == '3':
            print("Terima kasih! Sampai jumpa.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-3.")

if __name__ == "__main__":
    main()

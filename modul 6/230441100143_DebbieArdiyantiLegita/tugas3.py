barang = []

def tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    id_barang = input("Masukkan ID barang: ")
    prioritas = input("Pilih tingkat prioritas (Darurat/Biasa/Non-Darurat): ")
    
    data_barang = (nama_barang, id_barang, prioritas)
    
    if prioritas == "Darurat":
        barang.insert(0, data_barang)
    elif prioritas == "Biasa":
        for i, data in enumerate(barang):
            if data[2] == "Non-Darurat":
                barang.insert(i, data_barang)
                break
        else:
            barang.append(data_barang)
    elif prioritas == "Non-Darurat":
        barang.append(data_barang)
    else:
        print("Tingkat prioritas tidak valid.")
        return
    
    print("Data barang berhasil ditambahkan.")

def tampilkan_barang():
    if not barang:
        print("Belum ada data barang.")
    else:
        print("Data barang:")
        for data in barang:
            print(f"Nama Barang: {data[0]}")
            print(f"ID Barang: {data[1]}")
            print(f"Tingkat Prioritas: {data[2]}")
            print()

while True:
    print("Menu:")
    print("1. Tambah Barang")
    print("2. Lihat Data Barang")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        tampilkan_barang()
    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
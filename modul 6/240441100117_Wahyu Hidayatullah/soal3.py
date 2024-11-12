data_barang = []
def tambah_barang(data_barang):
    nama_barang = input("Masukkan Nama Barang: ")
    ID_barang = input("Masukkan ID Barang: ")
    prioritas = input("Masukkan Tingkat Prioritas (Darurat/Biasa/Non-Darurat): ")
    barang = (nama_barang, ID_barang, prioritas)
    if prioritas == "Darurat":
        data_barang.insert(barang)
    elif prioritas == "Biasa":
        posisi = 0
        for i, item in enumerate(data_barang):
            if item[2] == "Darurat":
                posisi = i + 1
        data_barang.insert(posisi, barang)
    elif prioritas == "Non-Darurat":
        data_barang.append(barang)
    else:
        print("Prioritas tidak valid. Silakan pilih antara 'Darurat', 'Biasa', atau 'Non-Darurat'.")
        return  
    print("Data barang berhasil ditambahkan")
def tampilkan_barang(data_barang):
    for nomor, barang in enumerate(data_barang, 1): 
        print(f"{nomor}. Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")
    print() 
def menu():
    while True:
        tambah_barang(data_barang)  
        tampilkan_barang(data_barang) 

        lagi = input("Apakah Anda ingin menambahkan barang lagi? (ya/tidak): ")
        if lagi.lower() == "ya":
            continue 
        elif lagi.lower() == "tidak":
            print("Program selesai.")  
            break  
        else:
            print("Pilihan tidak valid, program selesai.")  
            break
menu()
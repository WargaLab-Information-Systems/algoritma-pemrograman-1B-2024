data_barang = []

def tambah_barang(data_barang):
    nama_barang = input("Masukkan Nama Barang : ")
    ID_barang = input("Masukkan ID Barang : ")
    prioritas = input("Masukkan Tingkat Prioritas (Darurat/Biasa/Non-Darurat) : ")

    barang = (nama_barang, ID_barang, prioritas)

    if prioritas == "Darurat":
        data_barang.insert(0, barang)
    elif prioritas == "Biasa":
        index = next((i for i, b in enumerate(data_barang) if b[2] == "Non-Darurat"), len(data_barang))
        data_barang.insert(index, barang)
    elif prioritas == "Non-Darurat":
        data_barang.append(barang)
    else:
        print("Prioritas tidak valid. Silakan pilih antara 'Darurat', 'Biasa', atau 'Non-Darurat'.")
        return

    print("Data barang berhasil ditambahkan.\n")

def tampilkan_barang(data_barang):
    for nomor, barang in enumerate(data_barang, 1):
        print(f"{nomor}.Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")
    print()

def menu():
    while True:
        tambah_barang(data_barang)
        tampilkan_barang(data_barang)

        lagi = input("Apakah Anda ingin menambahkan barang lagi? (y/n) : ")
        if lagi == "y":
            continue
        elif lagi == "n":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, program selesai.")
            break

menu()

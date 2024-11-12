data_barang = []

def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    print("Pilih Tingkat Prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    prioritas = input("Pilih (1/2/3): ")

    barang = (id_barang, nama_barang, prioritas)
    
    if prioritas == "1": 
        data_barang.insert(0, barang)
    elif prioritas == "2": 
        tengah = len(data_barang)//2
        data_barang.insert(tengah, barang)
    elif prioritas == "3": 
        data_barang.append(barang)
    else:
        print("Pilihan prioritas tidak valid!")

    print("\nBarang berhasil ditambahkan.")
n = 1
n += 1
def tampilkan_semua_barang():
        if not data_barang:
            print("\nTidak ada data barang.")
        else:
            print("\nData Barang:")
        for barang in data_barang:
            if barang[2] == "1":
                prioritas_str = "Darurat"
            elif barang[2]== "2":
                prioritas_str = "Biasa"
            else:
                prioritas_str = "Non-Darurat"
            print(f"{n}. ID: {barang[0]}, Nama: {barang[1]}, Prioritas: {prioritas_str}")
while True:
    tambah_barang()
    tampilkan_semua_barang()
    lanjut = input("Apakah Anda ingin menambah barang lagi? (y/n): ").lower()
    if lanjut != "y":
        print("terima kasih,program selesai!!")
        break




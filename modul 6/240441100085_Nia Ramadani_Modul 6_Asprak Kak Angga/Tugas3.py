print("===DATA BARANG PRIORITAS===")
darurat = []
biasa = []
non_darurat = []

def tambah_dan_tampilkan_barang():

    id_barang = input("Masukkan ID Barang: ")
    nama_barang = input("Masukkan Nama Barang: ")
    prioritas = input("Masukkan Prioritas (1: Darurat, 2: Biasa, 3: Non-Darurat): ")

    if prioritas == "1":
        darurat.append((id_barang, nama_barang, "Darurat"))
    elif prioritas == "2":
        biasa.append((id_barang, nama_barang, "Biasa"))
    elif prioritas == "3":
        non_darurat.append((id_barang, nama_barang, "Non-Darurat"))
    else:
        print("Pilihan tidak valid. Data tidak ditambahkan.")
        return

    semua_barang = darurat + biasa + non_darurat

    print("\nDaftar Barang:")
    
    for index, barang in enumerate(semua_barang, 1):
        print(f"{index}.ID: {barang[0]}, Nama: {barang[1]}, Prioritas: {barang[2]}")
        


while True:
    tambah_dan_tampilkan_barang()
    lanjut = input("\nTambah barang lagi? (Ya/Tidak): ")
    if lanjut . lower () == 'Tidak':
        print("Program selesai.")
        break
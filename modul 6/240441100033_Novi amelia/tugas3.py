def tambah_barang(daftar_barang_darurat, daftar_barang_biasa, daftar_barang_non_darurat):
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    
    # Meminta input prioritas
    print("Pilih Tingkat Prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    pilihan_prioritas = input("Masukkan pilihan (1-3): ")

    # Menentukan prioritas
    if pilihan_prioritas == '1':
        prioritas = "Darurat"
        daftar_barang_darurat.append((nama_barang, id_barang, prioritas))
    elif pilihan_prioritas == '2':
        prioritas = "Biasa"
        daftar_barang_biasa.append((nama_barang, id_barang, prioritas))
    elif pilihan_prioritas == '3':
        prioritas = "Non-Darurat"
        daftar_barang_non_darurat.append((nama_barang, id_barang, prioritas))
    else:
        print("Pilihan tidak valid. Barang tidak ditambahkan.")
        return
    print("Barang berhasil ditambahkan.")

def tampilkan_barang(daftar_barang_darurat, daftar_barang_biasa, daftar_barang_non_darurat):
    if not (daftar_barang_darurat or daftar_barang_biasa or daftar_barang_non_darurat):
        print("Tidak ada barang yang disimpan.")
        return

    print("\nDaftar Barang:")
    for barang in daftar_barang_darurat:
        print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")
    for barang in daftar_barang_biasa:
        print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")
    for barang in daftar_barang_non_darurat:
        print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

def barang():
    daftar_barang_darurat = []
    daftar_barang_biasa = []
    daftar_barang_non_darurat = []
    while True:
        tambah_barang(daftar_barang_darurat, daftar_barang_biasa, daftar_barang_non_darurat)
        tampilkan_barang(daftar_barang_darurat, daftar_barang_biasa, daftar_barang_non_darurat)
        lagi = input("\nApakah Anda ingin menambahkan barang lagi? (y/n): ")
        if lagi != 'y':
            print("Terima kasih! Program selesai.")
            break
# Menjalankan fungsi utama
barang()
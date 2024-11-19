# List untuk menyimpan data barang
barang_list = []

# Fungsi untuk menambahkan barang
def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    print("Pilih tingkat prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    prioritas = input("Masukkan pilihan prioritas (1/2/3): ")

    # Membuat tuple data barang
    barang = (nama_barang, id_barang, prioritas)

    # Menyimpan barang berdasarkan prioritas
    if prioritas == '1':  # Darurat
        barang_list.insert(0, barang)  # Menambah di awal list
    elif prioritas == '2':  # Biasa
        barang_list.insert(len(barang_list)//2, barang)  # Menambah di tengah list
    elif prioritas == '3':  # Non-Darurat
        barang_list.append(barang)  # Menambah di akhir list
    else:
        print("Prioritas tidak valid, barang tidak ditambahkan.")
        return

    print("Barang berhasil ditambahkan.\n")

# Fungsi untuk menampilkan semua barang
def tampilkan_barang():
    if not barang_list:
        print("Tidak ada barang yang disimpan.\n")
    else:
        print("\nDaftar Barang Pengiriman:")
        for barang in barang_list:
            prioritas_str = { '1': 'Darurat', '2': 'Biasa', '3': 'Non-Darurat' }
            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {prioritas_str[barang[2]]}")
    print()

# Fungsi utama untuk menjalankan program
def main():
    while True:
        tambah_barang()  # Menambahkan barang baru
        tampilkan_barang()  # Menampilkan daftar barang

        # Menanyakan apakah ingin menambah barang lagi
        lanjutkan = input("Apakah Anda ingin menambah barang lagi? (y/n): ")
        if lanjutkan.lower() != 'y':
            print("Program selesai. Terima kasih.")
            break

if __name__ == "__main__":
    main()

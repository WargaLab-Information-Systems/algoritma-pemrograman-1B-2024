def tambah_barang(barang_list):
    nama = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Pilih Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ")

    if prioritas not in ["Darurat", "Biasa", "Non-Darurat"]:
        print("Prioritas tidak valid. Silakan coba lagi.")
        return

    barang_baru = (nama, id_barang, prioritas)

    if prioritas == "Darurat":
        barang_list.insert(0, barang_baru)  
    elif prioritas == "Biasa":
        # Tambahkan di tengah
        if len(barang_list) == 0:
            barang_list.append(barang_baru)
        else:
            barang_list.insert(len(barang_list) // 2, barang_baru)  # Tambahkan di tengah
    elif prioritas == "Non-Darurat":
        barang_list.append(barang_baru)  # Tambahkan di akhir


def tampilkan_barang(barang_list):
    print("\nDaftar Barang:")
    for barang in barang_list:
        print(f"{barang[0]} (ID: {barang[1]}, Prioritas: {barang[2]})")


def main():
    barang_list = []

    while True:
        tambah_barang(barang_list)
        tampilkan_barang(barang_list)

        lagi = input("Apakah Anda ingin menambah barang lagi? (y/n): ")
        if lagi.lower() != 'y':
            break
main()
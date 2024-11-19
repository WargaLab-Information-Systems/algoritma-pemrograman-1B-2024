def tambah_barang(barang_list):
    # Input data barang
    nama_barang = input("Masukkan nama barang: ")
    id_barang = input("Masukkan ID barang: ")
    
    # Memilih tingkat prioritas
    print("Pilih tingkat prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    pilihan = input("Masukkan pilihan (1/2/3): ")
    
    # Menentukan tingkat prioritas
    if pilihan == '1':
        prioritas = "Darurat"
    elif pilihan == '2':
        prioritas = "Biasa"
    elif pilihan == '3':
        prioritas = "Non-Darurat"
    else:
        print("Pilihan tidak valid. Barang tidak ditambahkan.")
        return
    
    # Menyimpan barang berdasarkan prioritas
    barang = (nama_barang, id_barang, prioritas)
    
    if prioritas == "Darurat":
        barang_list.insert(0, barang)  # insert ini digunakan untuk menyisipkan elemen baru pada posisi yang ditentukan oleh indeks 
    elif prioritas == "Biasa":
        # Tambahkan di tengah (setelah barang darurat)
        if len(barang_list) == 0 or barang_list[0][2] == "Non-Darurat": #digunakan untuk memeriksa kondisi tertentu dalam program sebelum menambahkan barang dengan prioritas "Biasa"
            barang_list.append(barang)  # Jika tidak ada barang darurat, tambahkan di akhir
        else:
            barang_list.insert(1, barang)  # Tambahkan setelah barang darurat
    elif prioritas == "Non-Darurat":
        barang_list.append(barang)  # Tambahkan di akhir, digunakan untuk menambahkan elemen baru

def tampilkan_barang(barang_list):
    print("\nDaftar Barang:")
    for barang in barang_list:
        print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

def main():
    barang_list = []
    
    while True:
        tambah_barang(barang_list)
        tampilkan_barang(barang_list)
        
        # Menanyakan apakah ingin menambah barang lagi
        lagi = input("\nApakah Anda ingin menambah barang lagi? (ya/tidak): ")
        if lagi != 'ya':
            break

    print("\nProgram selesai. Terima kasih!")

if __name__ == "__main__":
    main()
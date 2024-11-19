# List untuk menyimpan data barang berdasarkan prioritas
data_barang = []

# Fungsi untuk menambah barang sesuai prioritas
def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Masukkan Tingkat Prioritas (Darurat/Biasa/Non-Darurat): ").strip().lower()
    
    # Validasi prioritas
    if prioritas not in ["darurat", "biasa", "non-darurat"]:
        print("Prioritas tidak valid. Data barang tidak disimpan.\n")
        return
    
    # Membuat data barang sebagai tuple
    barang = (nama_barang, id_barang, prioritas)
    data_barang.append(barang)
    
    # Mengurutkan data_barang berdasarkan prioritas
    data_barang.sort(key=lambda x: {"darurat": 0, "biasa": 1, "non-darurat": 2}[x[2]])
    print("Data barang berhasil ditambahkan.\n")

# Fungsi untuk menampilkan semua barang yang telah diinputkan
def tampilkan_barang():
    if data_barang:
        print("\nData Barang:")
        for barang in data_barang:
            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")
    else:
        print("Belum ada data barang.\n")

# Main program
while True:
    tambah_barang()
    tampilkan_barang()
    
    ulangi = input("\nApakah ingin mengisi data barang lagi? (y/n): ").strip().lower()
    if ulangi != "y":
        print("Terima kasih! Program selesai.")
        break

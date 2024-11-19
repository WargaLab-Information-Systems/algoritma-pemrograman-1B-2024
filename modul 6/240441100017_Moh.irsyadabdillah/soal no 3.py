# List untuk menyimpan data barang
data_barang = []

# Fungsi untuk menambahkan barang berdasarkan prioritas
def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Masukkan Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ").lower()
    
    # Membuat data barang dalam bentuk dictionary
    barang = {"Nama Barang": nama_barang, "ID Barang": id_barang, "Prioritas": prioritas}
    print(barang)
    
#     # Menyimpan barang di list sesuai dengan prioritas
#     if prioritas == "darurat":
#         data_barang.insert(0, barang)  # Ditambahkan di awal list
#     elif prioritas == "biasa":
#         # Cari posisi terakhir dari barang dengan prioritas darurat
#         posisi_biasa = len([b for b in data_barang if b['Prioritas'] == "darurat"])
#         data_barang.insert(posisi_biasa, barang)  # Ditambahkan setelah barang darurat
#     elif prioritas == "non-darurat":
#         data_barang.append(barang)  # Ditambahkan di akhir list
#     else:
#         print("Prioritas tidak valid. Data barang tidak ditambahkan.")
#         return
    
#     print("Data barang berhasil ditambahkan.")

# # Fungsi untuk menampilkan seluruh data barang
# def tampilkan_barang():
#     if not data_barang:
#         print("Belum ada data barang yang ditambahkan.")
#     else:
#         print("\nDaftar Barang:")
#         for barang in data_barang:
#             print(f"Nama Barang: {barang['Nama Barang']}, ID Barang: {barang['ID Barang']}, Prioritas: {barang['Prioritas']}")

# # Main program
# while True:
#     tambah_barang()
#     tampilkan_barang()
    
#     lanjut = input("\nApakah Anda ingin menambahkan barang lagi? (y/n): ").lower()
#     if lanjut != 'y':
#         print("Program selesai.")
#         break
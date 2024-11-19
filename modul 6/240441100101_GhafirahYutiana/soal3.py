barang_list = []

def tampilkan_barang():
    print("\nDaftar Barang:")
    for idx, barang in enumerate(barang_list, 1):
        print(f"{idx}. Nama Barang: {barang['nama']}, ID Barang: {barang['id']}, Prioritas: {barang['prioritas']}")

def tambah_barang():
    nama = input("1. Masukkan Nama Barang: ")
    id_barang = input("2. Masukkan ID Barang: ")
    prioritas = input("3. Pilih prioritas (1=Darurat, 2=Biasa, 3=Non-Darurat): ")
    
    if prioritas == '1':
        Prioritas_barang = "Darurat"
    elif prioritas == '2':
        Prioritas_barang = "Biasa"
    else:
        Prioritas_barang = "Non-Darurat"

    barang_list.append({"nama": nama, "id": id_barang, "prioritas": Prioritas_barang})
    
    urutan_prioritas = {"Darurat": 1, "Biasa": 2, "Non-Darurat": 3}
    barang_list.sort(key=lambda x: urutan_prioritas[x["prioritas"]])

    tampilkan_barang()

while True:
    tambah_barang()
    if input("\nTambah barang lagi? (y/n): ").lower() != 'y':
        print("Program selesai.")
        break
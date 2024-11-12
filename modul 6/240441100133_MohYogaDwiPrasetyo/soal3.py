barang_list = []

def tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    id_barang = input("Masukkan ID barang: ")
    print("Pilih tingkat prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-darurat")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    # nentukan prioritas
    if pilihan == '1':
        prioritas = "Darurat"
        barang_list.insert(0, {"Nama": nama_barang, "ID": id_barang, "Prioritas": prioritas})
    elif pilihan == '2':
        prioritas = "Biasa"
        tengah = len(barang_list) // 2 # dpt kan nilai/indeks tngah
        barang_list.insert(tengah, {"Nama": nama_barang, "ID": id_barang, "Prioritas": prioritas})
    elif pilihan == '3':
        prioritas = "Non-Darurat"
        barang_list.append({"Nama": nama_barang, "ID": id_barang, "Prioritas": prioritas})
    else:
        print("Input tidak valid!!!")

def tampilkan_barang():
    if barang_list:
        print("\nDaftar barang: ")
        for barang in barang_list:
            print(f"Nama: {barang['Nama']}, ID: {barang['ID']}, Prioritas: {barang['Prioritas']}")
    else:
        print("Belum ada barang yang diinputkan.")

while True:
    tambah_barang()
    tampilkan_barang()
    ulang = input("\nApakah ingin menambah barang lagi? (y/n): ")
    if ulang == 'n':
        print("Terimakasih...")
        break
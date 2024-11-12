daftar_barang = []

def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Masukkan Tingkat Prioritas (Darurat/Biasa/Non-Darurat): ").lower()
    
    if prioritas == "darurat":
        daftar_barang.insert(0, (nama_barang, id_barang, prioritas))
    elif prioritas == "biasa":
        daftar_barang.append((nama_barang, id_barang, prioritas))
    elif prioritas == "non-darurat":
        daftar_barang.append((nama_barang, id_barang, prioritas))
    else:
        print("Prioritas tidak valid. Data tidak disimpan.")
    
    print("Data barang berhasil ditambahkan.")

def tampilkan_barang():
    if not daftar_barang:
        print("Belum ada barang yang disimpan.")
    else:
        print("\nDaftar Barang:")
        for barang in daftar_barang:
            print(f"Nama: {barang[0]}, ID: {barang[1]}, Prioritas: {barang[2]}")

while True:
    tambah_barang()
    tampilkan_barang()
    
    lanjut = input("\nApakah ingin menambah barang lagi? (ya/tidak): ").lower()
    if lanjut != 'ya':
        print("Program selesai.")
        break








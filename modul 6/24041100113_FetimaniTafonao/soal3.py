barang = []

def tambah_barang(nama, id_barang, prioritas):
    if prioritas == "Darurat":
        barang.insert(0, (nama, id_barang, prioritas))
    elif prioritas == "Biasa":
        barang.insert(len(barang) // 2, (nama, id_barang, prioritas))
    elif prioritas == "Non-Darurat":
        barang.append((nama, id_barang, prioritas))

def tampilkan_barang():
    print("\nDaftar Barang:")
    for item in barang:
        print(f"Nama Barang: {item[0]}, ID Barang: {item[1]}, Prioritas: {item[2]}")

while True:
    nama = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Masukkan Prioritas (Darurat/Biasa/Non-Darurat): ")
    tambah_barang(nama, id_barang, prioritas)
    tampilkan_barang()
    
    lagi = input("Apakah ingin menambah barang lagi? (ya/tidak): ").lower()
    if lagi != "ya":
        break

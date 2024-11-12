daftar_barang = []

def tambah_barang(darurat, biasa,non_darurat):
    nama_barang = input("Masukkan nama barang: ")
    id_barang = input("Masukkan ID barang: ")
    prioritas = input("Masukkan tingkat prioritas barang(Darurat/Biasa/Non-Darurat): ")

    if prioritas == "Darurat":
        darurat.append((nama_barang,id_barang,prioritas))
    elif prioritas == "Biasa":
        biasa.append((nama_barang,id_barang,prioritas))
    elif prioritas == "Non-Darurat":
        non_darurat.append((nama_barang,id_barang,prioritas))
    else:
        print("!!!Prioritas tidak valid!!!")

    return darurat, biasa, non_darurat

def tampilkan_barang(darurat,biasa,non_darurat):
    print()
    print("="*20)
    print("Daftar barang sesuai tingkat prioritas")
    
    for barang in darurat:
        print(f"Nama = {barang[0]}, ID = {barang[1]}, prioritas = {barang[2]}")

    for barang in biasa:
        print(f"Nama = {barang[0]}, ID = {barang[1]}, prioritas = {barang[2]}")

    for barang in non_darurat:
        print(f"Nama = {barang[0]}, ID = {barang[1]}, prioritas = {barang[2]}")
        print("="*20)

def menu():
    darurat = []
    biasa = []
    non_darurat = []
    while True: 
        darurat,biasa,non_darurat=tambah_barang(darurat,biasa,non_darurat)
        tampilkan_barang(darurat, biasa, non_darurat)

        lagi = input("Apakah anda ingin menambahkan barang lagi(y/n): ")
        if lagi == "y":
            continue
        elif lagi == "n":
            print("Terimakasih. Program selesai!!")
            break
        else:
            print("Pilihan tidak valid. Program selesai!!")
            break

menu()
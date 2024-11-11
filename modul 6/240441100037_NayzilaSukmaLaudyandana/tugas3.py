daftar_barang_darurat = []
daftar_barang_biasa = []
daftar_barang_non_darurat = []

def tambah_barang():
    nama = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Pilih Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ").lower()
    
    barang = {"Nama": nama, "ID": id_barang, "Prioritas": prioritas}
 
    if prioritas == "darurat":
        daftar_barang_darurat.append(barang)
    elif prioritas == "biasa":
        daftar_barang_biasa.append(barang)
    else:
        daftar_barang_non_darurat.append(barang)

def tampilkan_barang():
    print("\nDaftar Barang yang Telah Diinput:")
    
    for barang in daftar_barang_darurat:
        print(f"Nama: {barang['Nama']}, ID: {barang['ID']}, Prioritas: {barang['Prioritas']}")
    
    for barang in daftar_barang_biasa:
        print(f"Nama: {barang['Nama']}, ID: {barang['ID']}, Prioritas: {barang['Prioritas']}")
    
    for barang in daftar_barang_non_darurat:
        print(f"Nama: {barang['Nama']}, ID: {barang['ID']}, Prioritas: {barang['Prioritas']}")
    print()

while True:
    tambah_barang()
    tampilkan_barang()
    
    ulang = input("Apakah ingin menambah barang lagi?: ")
    if ulang != "y" or ulang == "ya":
        break

print("Program selesai.")


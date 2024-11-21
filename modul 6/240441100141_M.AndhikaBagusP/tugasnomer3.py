def tambah_barang(list_barang, namaBarang, idBarang, tingkatPrioritas):
    if tingkatPrioritas == "darurat":
        list_barang.insert(0, (namaBarang, idBarang, tingkatPrioritas))
    elif tingkatPrioritas == "biasa":
        index = 0
        while index < len(list_barang) and list_barang[index][2] == "darurat":
            index += 1
        list_barang.insert(index, (namaBarang, idBarang, tingkatPrioritas))
    elif tingkatPrioritas == "non-darurat":
        list_barang.append((namaBarang, idBarang, tingkatPrioritas))
    else:
        print("Tingkat prioritas tidak sesuai")
        
def tampilkan_barang(list_barang):
    print("List Barang: ")
    for i in list_barang:
        print(f"Barang: {i[0]}, ID barang: {i[1]}, Tingkat Prioritas: {i[2]}")
        
list_barang = []
while True:
    namaBarang = input("Masukkan nama barang: ")
    idBarang = input("Masukkan ID barang: ")
    tingkatPrioritas = input("Masukkan tingkat prioritas[Darurat/Biasa/Non-Darurat] :").lower()
    
    tambah_barang(list_barang, namaBarang, idBarang, tingkatPrioritas)
    tampilkan_barang(list_barang)

    repeat = input("Apakah anda ingin menambahkan barang lagi? [y/n]: ")
    if repeat == "n":
        break
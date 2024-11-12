# Menyimpan data barang
barang = []

# Menambahkan data barang (create)
def tambahkan_data():
    id = input("Masukkan ID Barang : ")
    nama = input("Masukkan Nama Barang : ")
    prioritas = input('''Tentukan Tingkat Prioritas :
          1. Darurat
          2. Biasa
          3. Non-Darurat
          Masukkan pilihanmu (1-3) : ''')

    # Menentukan prioritas berdasarkan input
    if prioritas == "1":
        prioritas = "Darurat"
        barang.insert(0, [id, nama, prioritas])  
    elif prioritas == "2":
        prioritas = "Biasa"
        index_awal = 0
        for i, biasa in enumerate(barang):
            if biasa[2] == "Darurat":  
                index_awal = i + 1
        barang.insert(index_awal, [id, nama, prioritas])  
    elif prioritas == "3":
        prioritas = "Non-Darurat"
        barang.append([id, nama, prioritas]) 
    else:
        print("Pilihan Anda Salah.")

# Menampilkan data barang
def tampilkan_data():
    if barang:
        print("Daftar Barang Ditampilkan:")
        for data in barang:
            print(f"ID Barang: {data[0]}, Nama Barang: {data[1]}, Tingkat Prioritas: {data[2]}")
    else:
        print("Belum Ada Data Barang")


while True:
    menu = input('''
        Program Pengelola Pengiriman Barang
                
                 1. Menambahkan Data Barang
                 2. Menampilkan Data Barang
                 3. Keluar dari Program
                
        Masukkan Menu Berdasarkan Kebutuhan (1-3) : ''')
    
    if menu == "1":
        tambahkan_data()
    elif menu == "2":
        tampilkan_data()
    elif menu == "3":
        print("Selesai.")
        break
    else:
        print("Maaf menu yang anda masukkan salah. Silahkan Coba Lagi.")

    ulang = input("Apakah Anda Ingin Mengelola Data Barang Lagi (y/n) : ")
    if ulang == "n":
        break
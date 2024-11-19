# List untuk menyimpan data barang
barang_list = []

# Fungsi untuk menampilkan daftar barang
def tampilkan_barang():
    if not barang_list:
        print("Belum ada barang yang ditambahkan.")
    else:
        print("\nDaftar Barang:")
        for barang in barang_list:
            print(f"Nama Barang: {barang['nama']}, ID Barang: {barang['id']}, Prioritas: {barang['prioritas']}")

# Fungsi untuk menambahkan barang
def tambah_barang():
    # Input data barang
    nama = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    
    # Memilih tingkat prioritas
    while True:
        print("\nPilih tingkat prioritas:")
        print("1. Darurat")
        print("2. Biasa")
        print("3. Non-Darurat")
        
        pilihan = input("Masukkan pilihan (1/2/3): ")
        
        if pilihan == '1':
            prioritas = "Darurat"
            # Tambahkan di awal list untuk prioritas Darurat
            barang_list.insert(0, {"nama": nama, "id": id_barang, "prioritas": prioritas})
            break

        elif pilihan == '2':
            prioritas = "Biasa"
            # Menghitung jumlah prioritas "darurat"
            jumlah_darurat = 0
            for p in barang_list:
                if p['prioritas'] == "Darurat":
                    jumlah_darurat += 1
            barang_list.insert(jumlah_darurat, {"nama": nama, "id": id_barang, "prioritas": prioritas})
            break

        elif pilihan == '3':
            prioritas = "Non-Darurat"
            # Tambahkan di akhir list untuk prioritas Non-Darurat
            barang_list.append({"nama": nama, "id": id_barang, "prioritas": prioritas})
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
    
    # Tampilkan daftar barang
    tampilkan_barang()

# Program utama
while True:
    tambah_barang()
    lagi = input("\nApakah Anda ingin menambahkan barang lagi? (y/n): ")
    if lagi.lower() != 'y':
        print("Terima kasih. Program selesai.")
        break
barang_list = []

def tampilkan_barang():
    if not barang_list:
        print("\nBelum ada barang yang terdaftar.")
    else:
        print("\nDaftar barang yang telah diinput:")
        for angka, barang in enumerate(barang_list, 1):
            print(f"{angka}. Nama: {barang['nama']}, ID: {barang['id']}, Prioritas: {barang['prioritas']}")

def tambah_barang(nama, id_barang, prioritas):
    barang = {'nama': nama, 'id': id_barang, 'prioritas': prioritas}
    
    if prioritas == 1:  
        barang['prioritas'] = 'Darurat'  
        barang_list.insert(0, barang)  
    elif prioritas == 2:  
        barang['prioritas'] = 'Biasa'  
        tengah = len(barang_list) // 2
        barang_list.insert(tengah, barang)  
    elif prioritas == 3: 
        barang['prioritas'] = 'Non-Darurat'  
        barang_list.append(barang)  

while True:
    print("\n=== Pengelola Pengiriman Barang ===")
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")

    print("\nPilih tingkat prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    
    prioritas = 0
    while prioritas not in [1, 2, 3]:
        prioritas = int(input("Masukkan kode prioritas (1/2/3): "))
        if prioritas not in [1, 2, 3]:
            print("Input tidak valid! Masukkan angka 1, 2, atau 3.")
    
    tambah_barang(nama_barang, id_barang, prioritas)
    
    tampilkan_barang()
    
    jawaban = input("\nApakah ingin menambah barang lagi? (y/n): ").lower()
    if jawaban != 'y':
        print("\nProgram selesai. Terima kasih!")
        break  


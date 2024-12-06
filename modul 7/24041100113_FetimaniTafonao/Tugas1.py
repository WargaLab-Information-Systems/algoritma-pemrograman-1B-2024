peminjaman = {
    'alat_pengukur_tekanan_darah': 0,
    'termometer': 0,
    'alat_pengukur_kadar_gula_darah': 0,
    'alat_pengukur_tensi': 0
}

def tampilkan_peminjaman():
    print("\nAlat kesehatan yang dipinjam saat ini:")
    ada_peminjaman = False
    for alat, jumlah in peminjaman.items():
        if jumlah > 0:
            print(f"{alat}: {jumlah}")
            ada_peminjaman = True
    if not ada_peminjaman:
        print("Tidak ada alat yang sedang dipinjam.")

while True:
    print("\nMenu:")
    print("1. Tambah alat yang dipinjam")
    print("2. Kurangi alat yang dipinjam (pengembalian)")
    print("3. Lihat daftar alat yang dipinjam")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        alat = input("Masukkan nama alat yang dipinjam: ").strip()
        jumlah = int(input(f"Masukkan jumlah {alat} yang ingin dipinjam: "))
        
        if alat in peminjaman:
            peminjaman[alat] += jumlah
            print(f"{jumlah} {alat} berhasil ditambahkan ke peminjaman.")
        else:
            print(f"{alat} tidak tersedia dalam daftar alat.")
    
    elif pilihan == "2":
        alat = input("Masukkan nama alat yang dikembalikan: ").strip()
        jumlah = int(input(f"Masukkan jumlah {alat} yang ingin dikembalikan: "))
        
        if alat in peminjaman:
            if peminjaman[alat] >= jumlah:
                peminjaman[alat] -= jumlah
                print(f"{jumlah} {alat} berhasil dikembalikan.")
            else:
                print(f"Jumlah pengembalian {alat} melebihi jumlah yang dipinjam.")
        else:
            print(f"{alat} tidak tersedia dalam daftar alat.")
    
    elif pilihan == "3":
        tampilkan_peminjaman()
    
    elif pilihan == "4":
        print("Terima kasih, program selesai.")
        break
    
    else:
        print("Pilihan tidak valid, silakan pilih menu yang tersedia.")

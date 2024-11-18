alat_kesehatan = {
    'pengukur tekanan darah': 0, 
    'termometer': 0,              
    'stetoskop': 0,     
    'alat inhaler': 0          
}

def pinjam_alat(jenis, jumlah):
    if jenis in alat_kesehatan:
        alat_kesehatan[jenis] += jumlah  
    else:
        alat_kesehatan[jenis] = jumlah  
    print(f"{jumlah} {jenis} berhasil ditambahkan.")

def kembalikan_alat(jenis, jumlah):
    if jenis in alat_kesehatan and alat_kesehatan[jenis] >= jumlah:
        alat_kesehatan[jenis] -= jumlah 
    print(f"{jumlah} {jenis} berhasil dikembalikan.")
    
def tukar_alat(jenis_baru, jumlah_baru, jenis_lama, jumlah_lama):
    kembalikan_alat(jenis_lama, jumlah_lama)  
    pinjam_alat(jenis_baru, jumlah_baru)   

    
def input_peminjaman():
    print("\nMasukkan jenis alat yang ingin dipinjam:")
    jenis = input("Pengukur Tekanan Darah, Termometer, Stetoskop, Alat Inhaler: ").lower()
    jumlah = int(input("Masukkan jumlah alat yang ingin dipinjam: "))
    
    if jenis in alat_kesehatan:
        pinjam_alat(jenis, jumlah)
    else:
        print("Jenis alat tidak valid!")

def input_pengembalian():
    print("\nMasukkan jenis alat yang ingin dikembalikan:")
    jenis = input("Pengukur Tekanan Darah, Termometer, Stetoskop, Alat Inhaler: ").lower()
    jumlah = int(input("Masukkan jumlah alat yang ingin dikembalikan: "))
    
    if jenis in alat_kesehatan:
        kembalikan_alat(jenis, jumlah)
    else:
        print("Jenis alat tidak valid!")

def input_penukaran():
    print("\nMasukkan jenis alat yang ingin ditukar:")
    jenis_lama = input("Pengukur Tekanan Darah, Termometer, Stetoskop, Alat Inhaler: ").lower()
    jumlah_lama = int(input("Masukkan jumlah alat lama yang ingin ditukar: "))
    jenis_baru = input("Masukkan jenis alat baru yang ingin dipinjam: ").lower()
    jumlah_baru = int(input("Masukkan jumlah alat baru yang ingin dipinjam: "))

    if jenis_lama in alat_kesehatan and jenis_baru in alat_kesehatan:
        tukar_alat(jenis_baru, jumlah_baru, jenis_lama, jumlah_lama)
    else:
        print("Jenis alat tidak valid!")

def tampilkan_alat():
    print("\nAlat kesehatan yang dipinjam Heni saat ini:")
    for alat, jumlah in alat_kesehatan.items():
        if jumlah > 0:
            print(f"{alat}: {jumlah}")

while True:
    print("\nMenu:")
    print("1. Pinjam alat")
    print("2. Kembalikan alat")
    print("3. Tukar alat")
    print("4. Lihat alat yang dipinjam")
    print("5. Keluar")
    
    pilihan = int(input("Pilih opsi (1-5): "))
    
    if pilihan == 1:
        input_peminjaman()  
    elif pilihan == 2:
        input_pengembalian() 
    elif pilihan == 3:
        input_penukaran()  
    elif pilihan == 4:
        tampilkan_alat()  
    elif pilihan == 5:
        print("Terima kasih! Program selesai.")
        break 
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
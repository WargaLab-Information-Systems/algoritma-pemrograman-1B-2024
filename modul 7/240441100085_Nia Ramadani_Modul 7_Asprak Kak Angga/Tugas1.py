alat_kesehatan = {
    "tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhealer": 0,
}

def tambah_alat():
    jenis = input("Masukkan jenis alat kesehatan: ")
    jumlah = int(input(f"Masukkan jumlah {jenis} yang ingin ditambahkan: "))
    if jenis in alat_kesehatan:
        alat_kesehatan[jenis] += jumlah
    else:
        alat_kesehatan[jenis] = jumlah
    print(f"{jumlah} {jenis} berhasil ditambahkan.")

def Mengembalikan_alat():
    jenis = input("Masukkan jenis alat kesehatan: ")
    jumlah = int(input(f"Masukkan jumlah {jenis} yang ingin dikembalikan: "))
    if jenis in alat_kesehatan and alat_kesehatan[jenis] >= jumlah:
        alat_kesehatan[jenis] -= jumlah
        if alat_kesehatan[jenis] == 0:
            alat_kesehatan.pop(jenis)
        print(f"{jumlah} {jenis} berhasil dikurangi.")
    else:
        print("Gagal mengurangi. Pastikan jenis dan jumlah alat benar.")

def tukar_alat():
    jenis_awal = input("Masukkan jenis alat yang ingin ditukar: ")
    jumlah_awal = int(input(f"Masukkan jumlah {jenis_awal} yang ingin ditukar: "))
    jenis_baru = input("Masukkan jenis alat baru: ")
    jumlah_baru = int(input(f"Masukkan jumlah {jenis_baru} yang ingin ditambahkan: "))

    if jenis_awal in alat_kesehatan and alat_kesehatan[jenis_awal] >= jumlah_awal:
        alat_kesehatan[jenis_awal] -= jumlah_awal
        if alat_kesehatan[jenis_awal] == 0:
            alat_kesehatan.pop(jenis_awal)

        if jenis_baru in alat_kesehatan:
            alat_kesehatan[jenis_baru] += jumlah_baru
        else:
            alat_kesehatan[jenis_baru] = jumlah_baru
        
        print(f"{jumlah_awal} {jenis_awal} berhasil ditukar dengan {jumlah_baru} {jenis_baru}.")
    else:
        print(f"Gagal menukar. Pastikan jumlah {jenis_awal} yang dimasukkan benar dan tersedia.")
def tampilkan_alat():
    print("\nAlat kesehatan yang dipinjam saat ini:")
    if alat_kesehatan:
        for jenis, jumlah in alat_kesehatan.items():
            print(f"{jenis}: {jumlah} buah")
    else:
        print("Tidak ada alat yang dipinjam.")


while True:
    print("\n=== Menu ===")
    print("1. Tambah alat kesehatan")
    print("2. Mengembalikan alat kesehatan")
    print("3. Tukar alat kesehatan")
    print("4. Tampilkan alat kesehatan")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        tambah_alat()
    elif pilihan == "2":
        Mengembalikan_alat()
    elif pilihan == "3":
        tukar_alat()
    elif pilihan == "4":
        tampilkan_alat()
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")
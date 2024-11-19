alat_kesehatan = {
    "tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhealer": 0,
}

def pinjam_alat():
    nama_alat = input("Masukkan nama alat kesehatan: ")
    jumlah = int(input(f"Masukkan jumlah {nama_alat} yang ingin ditambahkan: "))
    if nama_alat in alat_kesehatan:
        alat_kesehatan[nama_alat] += jumlah
    else:
        alat_kesehatan[nama_alat] = jumlah
    print(f"{jumlah} {nama_alat} berhasil ditambahkan.")

def kembalikan_alat():
    nama_alat = input("Masukkan nama alat kesehatan: ")
    jumlah = int(input(f"Masukkan jumlah {nama_alat} yang ingin dikembalikan: "))
    if nama_alat in alat_kesehatan and alat_kesehatan[nama_alat] >= jumlah:
        alat_kesehatan[nama_alat] -= jumlah
        if alat_kesehatan[nama_alat] == 0:
            alat_kesehatan.pop(nama_alat)
        print(f"{jumlah} {nama_alat} berhasil dikurangi.")
    else:
        print("Tidak dapat mengurangi. Pastikan nama alat dan jumlah alat benar.")

def tukar_alat():
    nama_alat_awal = input("Masukkan nama alat yang ingin ditukar: ")
    jumlah_awal = int(input(f"Masukkan jumlah {nama_alat_awal} yang ingin ditukar: "))
    nama_alat_baru = input("Masukkan nama alat baru: ")
    jumlah_baru = int(input(f"Masukkan jumlah {nama_alat_baru} yang ingin ditambahkan: "))

    if nama_alat_awal in alat_kesehatan and alat_kesehatan[nama_alat_awal] >= jumlah_awal:
        alat_kesehatan[nama_alat_awal] -= jumlah_awal
        if alat_kesehatan[nama_alat_awal] == 0:
            alat_kesehatan.pop(nama_alat_awal)

        if nama_alat_baru in alat_kesehatan:
            alat_kesehatan[nama_alat_baru] += jumlah_baru
        else:
            alat_kesehatan[nama_alat_baru] = jumlah_baru
        
        print(f"{jumlah_awal} {nama_alat_awal} berhasil ditukar dengan {jumlah_baru} {nama_alat_baru}.")
    else:
        print(f"Gagal menukar. Pastikan jumlah {nama_alat_awal} yang dimasukkan benar dan tersedia.")

def tampilkan_alat():
    print("Alat kesehatan yang dipinjam saat ini:")
    if alat_kesehatan:
        for nama_alat, jumlah in alat_kesehatan.items():
            print(f"{nama_alat}: {jumlah} buah")
    else:
        print("Tidak ada alat yang dipinjam.")


while True:
    print("\nMenu:")
    print("1. Pinjam alat kesehatan")
    print("2. Kembalikan alat kesehatan")
    print("3. Tukar alat kesehatan")
    print("4. Tampilkan alat kesehatan")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        pinjam_alat()
    elif pilihan == "2":
        kembalikan_alat()
    elif pilihan == "3":
        tukar_alat()
    elif pilihan == "4":
        tampilkan_alat()
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")

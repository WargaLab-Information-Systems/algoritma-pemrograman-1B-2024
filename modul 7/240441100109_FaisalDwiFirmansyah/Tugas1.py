alat_kesehatan = {
    "pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0
}

daftar_alat = [
    "pengukur tekanan darah",
    "termometer",
    "stetoskop",
    "inhaler"
]

def pinjam_alat(nama_alat, jumlah):
    alat_kesehatan[nama_alat] += jumlah
    print(f"{jumlah} {nama_alat} berhasil ditambahkan!")

def tampilkan_alat():
    if all(jumlah == 0 for jumlah in alat_kesehatan.values()):
        print("\nBelum ada peminjaman.")
    else:
        print("\nAlat kesehatan yang masih dipinjam:")
        for alat, jumlah in alat_kesehatan.items():
            if jumlah > 0:
                print(f"{alat}: {jumlah} buah")
    print()

def kembalikan_alat(nama_alat, jumlah):
    if alat_kesehatan[nama_alat] >= jumlah:
        alat_kesehatan[nama_alat] -= jumlah
        print(f"{jumlah} {nama_alat} berhasil dikembalikan!")
    else:
        print(f"Gagal mengembalikan {nama_alat}. Jumlah tidak mencukupi.")

def hapus_semua_alat():
    alat_kesehatan.clear()
    print("Semua data alat telah dihapus.")

def tukar_alat(alat_ditukar, jumlah_tukar, alat_baru, jumlah_baru):
    if alat_kesehatan[alat_ditukar] >= jumlah_tukar:
        alat_kesehatan[alat_ditukar] -= jumlah_tukar
        alat_kesehatan[alat_baru] += jumlah_baru
        print(f"{jumlah_tukar} {alat_ditukar} berhasil ditukar dengan {jumlah_baru} {alat_baru}!")
    else:
        print(f"Gagal menukar {alat_ditukar}. Jumlah tidak mencukupi.")

def pilih_alat():
    print("\nPilih alat:")
    for i, alat in enumerate(daftar_alat, start=1):
        print(f"{i}. {alat}")
    pilihan = int(input("Masukkan nomor alat: ")) - 1
    if 0 <= pilihan < len(daftar_alat):
        return daftar_alat[pilihan]
    else:
        print("Pilihan tidak valid.")
        return None

def menu():
    while True:
        print("\n=== Menu Alat Kesehatan ===")
        print("1. Tambah alat (pinjam)")
        print("2. Tampilkan alat yang dipinjam")
        print("3. Kembalikan alat")
        print("4. Hapus semua data alat")
        print("5. Tukar alat")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            nama_alat = pilih_alat()
            if nama_alat:
                jumlah = int(input(f"Masukkan jumlah {nama_alat} yang dipinjam: "))
                pinjam_alat(nama_alat, jumlah)

        elif pilihan == '2':
            tampilkan_alat()

        elif pilihan == '3':
            nama_alat = pilih_alat()
            if nama_alat:
                jumlah = int(input(f"Masukkan jumlah {nama_alat} yang dikembalikan: "))
                kembalikan_alat(nama_alat, jumlah)

        elif pilihan == '4':
            konfirmasi = input("Apakah Anda yakin ingin menghapus semua data? (y/n): ").lower()
            if konfirmasi == 'y':
                hapus_semua_alat()

        elif pilihan == '5':
            print("\nPilih alat yang ingin ditukar:")
            alat_ditukar = pilih_alat()
            if alat_ditukar:
                jumlah_tukar = int(input(f"Masukkan jumlah {alat_ditukar} yang ditukar: "))
                print("\nPilih alat yang ingin diperoleh:")
                alat_baru = pilih_alat()
                if alat_baru:
                    jumlah_baru = int(input(f"Masukkan jumlah {alat_baru} yang diperoleh: "))
                    tukar_alat(alat_ditukar, jumlah_tukar, alat_baru, jumlah_baru)

        elif pilihan == '6':
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
menu()

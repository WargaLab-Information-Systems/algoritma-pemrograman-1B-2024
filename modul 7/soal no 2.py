# Struktur data untuk menyimpan klub dan anggotanya
klub = {
    "Basket": set(),
    "Renang": set()
}

# Fungsi untuk menambahkan anggota ke klub
def tambah_anggota(nama, klub_nama):
    if klub_nama in klub:
        klub[klub_nama].add(nama)
    else:
        print(f"Klub {klub_nama} tidak ditemukan.")

# Fungsi untuk menampilkan anggota klub
def tampilkan_anggota(klub_nama):
    if klub_nama in klub:
        return klub[klub_nama]
    else:
        return f"Klub {klub_nama} tidak ditemukan."

# Fungsi untuk menampilkan siswa yang mengikuti kedua klub
def siswa_kedua_klub():
    return klub["Basket"].intersection(klub["Renang"]) #digunakan untuk mengembalikan anggota yang terdaftar di kedua klub

# Fungsi untuk menampilkan siswa yang hanya mengikuti satu klub
def siswa_hanya_satu_klub():
    hanya_basket = klub["Basket"].difference(klub["Renang"]) # untuk menemukan anggota yang ada dalam set klub Renang tetapi tidak ada dalam set klub Basket.
    hanya_renang = klub["Renang"].difference(klub["Basket"])
    return hanya_basket.union(hanya_renang) # akan menggabungkan semua siswa yang hanya terdaftar di klub Basket dengan semua siswa yang hanya terdaftar di klub Renang.

# Fungsi untuk menampilkan semua siswa unik
def semua_siswa_unik():
    return klub["Basket"].union(klub["Renang"]) # untuk menggabungkan semua anggota klub basket dan renang

# Fungsi untuk menghitung jumlah siswa unik
def jumlah_siswa_unik():
    return len(semua_siswa_unik())  # len dibuat menghitung jumlah siswa yang unik

# Menu untuk interaksi dengan pengguna
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah anggota ke klub")
        print("2. Tampilkan anggota klub Basket")
        print("3. Tampilkan anggota klub Renang")
        print("4. Tampilkan siswa yang mengikuti kedua klub")
        print("5. Tampilkan siswa yang hanya mengikuti satu klub")
        print("6. Tampilkan semua siswa unik")
        print("7. Tampilkan jumlah siswa unik")
        print("8. Keluar")
        
        pilihan = input("Pilih opsi (1-8): ")
        
        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            klub_nama = input("Masukkan nama klub (Basket/Renang/ Kedua): ").strip().lower()
            if klub_nama == "basket":
                tambah_anggota(nama, "Basket")
            elif klub_nama == "renang":
                tambah_anggota(nama, "Renang")
            elif klub_nama == "kedua":
                tambah_anggota(nama, "Basket")
                tambah_anggota(nama, "Renang")
            else:
                print("Klub tidak valid. Silakan masukkan 'Basket', 'Renang', atau 'Kedua'.")
        elif pilihan == "2":
            print("Anggota klub Basket:", tampilkan_anggota("Basket"))
        elif pilihan == "3":
            print("Anggota klub Renang:", tampilkan_anggota("Renang"))
        elif pilihan == "4":
            print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub())
        elif pilihan == "5":
            print("Siswa yang hanya mengikuti satu klub:", siswa_hanya_satu_klub())
        elif pilihan == "6":
            print("Semua siswa unik yang mengikuti setidaknya satu klub:", semua_siswa_unik())
        elif pilihan == "7":
            print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik())
        elif pilihan == "8":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
main()
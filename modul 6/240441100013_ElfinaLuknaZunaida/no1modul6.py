daftar_karyawan = []

for i in range(5):
    print(f"Data Karyawan {i + 1}")
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")

    karyawan = {
        "nip": nip,
        "nama": nama,
        "alamat": alamat,
        "departemen": departemen,
        "jabatan": jabatan
    }
    daftar_karyawan.append(karyawan)
    print()

# Pencarian data 
while True:
    print("Pencarian Karyawan Berdasarkan Atribut")
    key_word = input("Masukkan kata untuk pencarian: ")

    ditemukan = False
    for karyawan in daftar_karyawan:
        if key_word in karyawan['nip'] or key_word in karyawan['nama'] or key_word in karyawan['alamat'] or key_word in karyawan['departemen'] or key_word in karyawan['jabatan']:
            print(f"NIP: {karyawan['nip']}, Nama: {karyawan['nama']}, Alamat: {karyawan['alamat']}, "
                  f"Departemen: {karyawan['departemen']}, Jabatan: {karyawan['jabatan']}")
            ditemukan = True

    if not ditemukan:
        print("Tidak ada karyawan yang sesuai dengan kriteria pencarian.")

    lanjut = input("Apakah ingin melakukan pencarian lagi? (ya/tidak): ").lower()
    if lanjut != 'ya':
        break

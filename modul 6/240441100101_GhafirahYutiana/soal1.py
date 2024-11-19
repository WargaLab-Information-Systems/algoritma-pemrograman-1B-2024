data_karyawan = []

for i in range(5):
    print(f"Masukkan data karyawan ke-{ i+1},")
    nip = input("NIP: ")
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    departemen = input("Departemen: ")
    jabatan = input("Jabatan: ")
    print("==========")
    
    data_karyawan.append([nip, nama, alamat, departemen, jabatan])

def tampilkan_semua_karyawan():
    if not data_karyawan:
        print("Belum ada data karyawan.")
    else:
        print("\nData Semua Karyawan:")
        for i, karyawan in enumerate(data_karyawan, start=1):
            print(f"Karyawan {i}: NIP: {karyawan[0]}, Nama: {karyawan[1]}, "
                  f"Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def cari_karyawan(atribut, nilai):
    indeks = ["nip", "nama", "alamat", "departemen", "jabatan"].index(atribut)
    hasil_cari = [k for k in data_karyawan if k[indeks] == nilai]
    
    if hasil_cari:
        print("\nHasil pencarian:")
        for karyawan in hasil_cari:
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, "
                  f"Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
    else:
        print("Tidak ada karyawan yang sesuai.")

while True:
    print("\nMenu:")
    print("1. Tampilkan semua karyawan")
    print("2. Cari karyawan berdasarkan atribut")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_semua_karyawan()
    elif pilihan == "2":
        atribut = input("Masukkan atribut yang ingin dicari (nip/nama/alamat/departemen/jabatan): ").lower()
        nilai = input(f"Masukkan nilai {atribut} yang ingin dicari: ")
        cari_karyawan(atribut, nilai)
    elif pilihan == "3":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        
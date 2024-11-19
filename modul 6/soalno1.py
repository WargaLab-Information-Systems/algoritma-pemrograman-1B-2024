data_karyawan = []

for i in range(5):
    print(f"\nInput Data Karyawan {i+1}") 
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")
    
    karyawan = {
        "NIP": nip,
        "Nama": nama,
        "Alamat": alamat,
        "Departemen": departemen,
        "Jabatan": jabatan
    }
    
    data_karyawan.append(karyawan)

# Fungsi pencarian berdasarkan atribut
def cari_karyawan(atribut, nilai):
    hasil_cari = [k for k in data_karyawan if k.get(atribut) == nilai]
    if hasil_cari:
        print("\nHasil Pencarian:")
        for karyawan in hasil_cari:
            print(f"NIP: {karyawan['NIP'  ]}, Nama: {karyawan['Nama']}, Alamat: {karyawan['Alamat']}, Departemen: {karyawan['Departemen']}, Jabatan: {karyawan['Jabatan']}")
    else:
        print("\nTidak ada karyawan yang ditemukan dengan kriteria tersebut.")

# Menu Pencarian
while True:
    print("\nPilih atribut untuk pencarian:")
    print("1. NIP")
    print("2. Nama")
    print("3. Alamat")
    print("4. Departemen")
    print("5. Jabatan")
    print("6. Keluar")
    pilihan = input("Masukkan pilihan (1-6): ")
    
    if pilihan == "6":
        break
    elif pilihan in ["1", "2", "3", "4", "5"]:
        atribut = ["NIP", "Nama", "Alamat", "Departemen", "Jabatan"][int(pilihan) - 1]
        nilai_cari = input(f"Masukkan nilai {atribut} yang dicari: ")
        cari_karyawan(atribut, nilai_cari)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

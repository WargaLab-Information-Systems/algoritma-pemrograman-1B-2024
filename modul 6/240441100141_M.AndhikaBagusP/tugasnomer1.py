dataKaryawan = []

def list_karyawan():
    for i in range (5):
        print(f"Masukkan data karyawan ke {i+1}")
        nip = input("Masukkan NIP: ")
        nama = input("Masukkan Nama: ").lower()
        alamat   = input("Masukkan Alamat: ").lower()
        departemen = input("Masukkan Departemen: ").lower()
        jabatan = input("Masukkan Jabatan: ").lower()
        dataKaryawan.append((nip, nama, alamat, departemen, jabatan)) 
        
def pencarian(dataKaryawan):
    print("==================")
    print("1. NIP")
    print("2. Nama")
    print("3. Alamat")
    print("4. Departemen")
    print("5. Jabatan")
    cariAtribut = input("Masukkan atribut yang anda cari (1-5): ")
    cariDataAtribut = input("Masukkan data sesuai atribut yang dicari: ").lower()
    
    for karyawan in dataKaryawan:
        if cariAtribut == "1" and cariDataAtribut == karyawan[0]:
            return karyawan
        if cariAtribut == "2" and cariDataAtribut == karyawan[1]:
            return karyawan
        if cariAtribut == "3" and cariDataAtribut == karyawan[2]:
            return karyawan
        if cariAtribut == "4" and cariDataAtribut == karyawan[3]:
            return karyawan
        if cariAtribut == "5" and cariDataAtribut == karyawan[4]:
            return karyawan
       
    return None

list_karyawan()

hasil = pencarian(dataKaryawan)
if hasil:
    print(hasil)
else:
    print("Data tidak ditemukan")
def input_data_karyawan():
    karyawan_list = []
    jumlah = int(input("Berapa data karyawan yang ingin anda masukkan? : "))
    for i in range(jumlah):
        print(f"MASUKKAN DATA KARYAWAN KE-{i + 1}")
        nip = input("Masukkan NIP : ")
        nama = input("Masukkan Nama : ")
        alamat = input("Masukkan Alamat : ")
        departemen = input("Masukkan Departemen : ")
        jabatan = input("Masukkan Jabatan : ")
        karyawan_list.append((nip, nama, alamat, departemen, jabatan)) 
    return karyawan_list

def cari_karyawan(karyawan_list, atribut, nilai_cari):
    indeks = {"nip": 0, "nama": 1, "alamat": 2, "departemen": 3, "jabatan": 4} 
    return [k for k in karyawan_list if str(k[indeks[atribut]]) == nilai_cari]

def tampilkan_karyawan(karyawan):
    print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def main(): 
    karyawan_list = input_data_karyawan() 
    while True:
        atribut = input("Pilih atribut yang ingin dicari(nip, nama, alamat, departemen, jabatan) : ")
        nilai_cari = input(f"Masukkan nilai {atribut} yang ingin dicari : ")
        
        hasil_pencarian = cari_karyawan(karyawan_list, atribut, nilai_cari) 
        if hasil_pencarian:
            print(f"DATA KARYAWAN DENGAN {atribut} '{nilai_cari}':")
            for karyawan in hasil_pencarian:
                tampilkan_karyawan(karyawan)
        else:
            print(f"Tidak ada data karyawan dengan {atribut} '{nilai_cari}'.")

        if input("Apakah anda ingin mencari lagi? (y/n): ") != 'y':
            break
main()
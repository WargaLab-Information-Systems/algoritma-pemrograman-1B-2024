karyawan = []
list_NIP = []
list_Nama = []
list_Alamat = []
list_Department = []
list_Jabatan = []

def input_nip():
    nip = int(input("Masukkan NIP: "))
    list_NIP.append(nip)

def input_nama():
    nama_input = input("Masukkan Nama: ")
    list_Nama.append(nama_input)

def input_alamat():
    alamat_input = input("Masukkan Alamat: ")
    list_Alamat.append(alamat_input)

def input_department():
    department_input = input("Masukkan Department: ")
    list_Department.append(department_input)

def input_jabatan():
    jabatan_input = input("Masukkan Jabatan: ")
    list_Jabatan.append(jabatan_input)

def data_karyawan(n=5):
    for i in range(n):
        input_nip()
        input_nama()
        input_alamat()
        input_department()
        input_jabatan()
        karyawan.append({
            'NIP': list_NIP[-1],
            'Nama': list_Nama[-1],
            'Alamat': list_Alamat[-1],
            'Department': list_Department[-1],
            'Jabatan': list_Jabatan[-1]
        })

def cari_karyawan(atribut, nilai):
    hasil_cari = []
    for data in karyawan:
        if str(data.get(atribut)) == str(nilai):  # Pastikan perbandingan tipe data konsisten
            hasil_cari.append(data)
    return hasil_cari
def tampilkan_semua_karyawan():
    if karyawan:
        print("Semua data karyawan:")
        for k in karyawan:
            print(k)
    else:
        print("Tidak ada data karyawan.")
def main():
    data_karyawan(n=5)

    while True:
        atribut = input("Masukkan atribut yang ingin dicari (NIP, Nama, Alamat, Department, Jabatan) atau 'exit' untuk keluar: ")
        if atribut.lower() == 'exit':
            tampilkan_semua_karyawan()
            break
        nilai = input(f"Masukkan nilai untuk {atribut}: ")
        
        # Cek apakah atribut yang dimasukkan valid
        if atribut in ['NIP', 'Nama', 'Alamat', 'Department', 'Jabatan']:
            if atribut == 'NIP':
                nilai = int(nilai)  # Konversi nilai ke integer jika atributnya NIP
            
            hasil = cari_karyawan(atribut, nilai)
            if hasil:
                for k in hasil:
                    print(k)
            else:
                print("Data tidak ditemukan.")
        else:
            print("Atribut tidak valid. Silakan coba lagi.")
main()
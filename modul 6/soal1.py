# # List untuk menyimpan data karyawan
# karyawan_list = []

# # Fungsi untuk menambahkan data karyawan
# def tambah_karyawan():
#     for i in range(5):
#         print(f"\nKaryawan ke-{i + 1}")
#         nip = input("Masukkan NIP: ")
#         nama = input("Masukkan Nama: ")
#         alamat = input("Masukkan Alamat: ")
#         departemen = input("Masukkan Departemen: ")
#         jabatan = input("Masukkan Jabatan: ")
        
#         # Simpan data karyawan sebagai dictionary
#         karyawan = {
#             "NIP": nip,
#             "Nama": nama,
#             "Alamat": alamat,
#             "Departemen": departemen,
#             "Jabatan": jabatan
#         }
#         # Tambahkan ke dalam list
#         karyawan_list.append(karyawan)

# # Fungsi untuk mencari data karyawan
# def cari_karyawan():
#     atribut = input("\nCari berdasarkan (NIP, Nama, Alamat, Departemen, Jabatan): ").capitalize()
#     nilai = input("Masukkan nilai pencarian: ")
    
#     # Hasil pencarian akan disimpan di list baru
#     hasil = []
#     for k in karyawan_list:
#         if atribut in k and k.get(atribut) == nilai:
#             hasil.append(k)

#     # Menampilkan hasil pencarian
#     if hasil:
#         print("\nHasil Pencarian:")
#         for k in hasil:
#             print(k)
#     else:
#         print("Tidak ada karyawan yang sesuai.")

# # Fungsi utama
# def main():
#     tambah_karyawan()
#     while True:
#         cari_karyawan()
#         if input("\nCari lagi? (y/n): ").lower() != 'y':
#             break

# if __name__ == "__main__":
#     main()






















# class Karyawan:
#     def __init__(self, nip, nama, alamat, departemen, jabatan):
#         self.nip = nip
#         self.nama = nama
#         self.alamat = alamat
#         self.departemen = departemen
#         self.jabatan = jabatan

#     def __repr__(self):
#         return f"NIP: {self.nip}, Nama: {self.nama}, Alamat: {self.alamat}, Departemen: {self.departemen}, Jabatan: {self.jabatan}"

# class Perusahaan:
#     def __init__(self):
#         self.karyawan_list = []

#     def tambah_karyawan(self, karyawan):
#         self.karyawan_list.append(karyawan)

#     def cari_karyawan(self, atribut, nilai):
#         hasil_pencarian = [karyawan for karyawan in self.karyawan_list if getattr(karyawan, atribut, None) == nilai]
#         if hasil_pencarian:
#             return hasil_pencarian
#         else:
#             return "Tidak ada karyawan yang sesuai dengan kriteria pencarian."

# def input_data_karyawan():
#     perusahaan = Perusahaan()
#     for i in range(5):
#         print(f"\nMasukkan data karyawan ke-{i+1}")
#         nip = input("NIP: ")
#         nama = input("Nama: ")
#         alamat = input("Alamat: ")
#         departemen = input("Departemen: ")
#         jabatan = input("Jabatan: ")
        
#         karyawan = Karyawan(nip, nama, alamat, departemen, jabatan)
#         perusahaan.tambah_karyawan(karyawan)
    
#     return perusahaan

# def main():
#     perusahaan = input_data_karyawan()

#     while True:
#         print("\nPencarian Karyawan")
#         print("Atribut yang dapat dicari: nip, nama, alamat, departemen, jabatan")
#         atribut = input("Masukkan atribut yang ingin dicari: ").lower()
#         nilai = input("Masukkan nilai pencarian: ")
        
#         hasil = perusahaan.cari_karyawan(atribut, nilai)
#         if isinstance(hasil, list):
#             print("\nHasil pencarian:")
#             for karyawan in hasil:
#                 print(karyawan)
#         else:
#             print(hasil)

#         lagi = input("Ingin mencari lagi? (y/n): ").lower()
#         if lagi != 'y':
#             break

# if __name__ == "__main__":
#     main()








































# Inisialisasi list untuk menyimpan data karyawan
karyawan_list = []

# Fungsi untuk menambahkan data karyawan
def tambah_karyawan():
    for i in range(5):
        print(f"\nMasukkan data karyawan ke-{i+1}")
        karyawan = {
            "NIP": input("NIP: "),
            "Nama": input("Nama: "),
            "Alamat": input("Alamat: "),
            "Departemen": input("Departemen: "),
            "Jabatan": input("Jabatan: ")
        }
        karyawan_list.append(karyawan)

# Fungsi untuk mencari karyawan berdasarkan atribut
def cari_karyawan(atribut, nilai):
    hasil = [k for k in karyawan_list if k[atribut] == nilai]
    return hasil if hasil else "Tidak ada karyawan yang sesuai."

# Fungsi utama untuk menjalankan program
def main():
    tambah_karyawan()
    
    while True:
        print("\nPencarian Karyawan")
        atribut = input("Masukkan atribut yang ingin dicari (NIP, Nama, Alamat, Departemen, Jabatan): ").capitalize()
        nilai = input("Masukkan nilai pencarian: ")
        
        hasil = cari_karyawan(atribut, nilai)
        
        if isinstance(hasil, list):
            print("\nHasil pencarian:")
            for k in hasil:
                print(k)
        else:
            print(hasil)

        lagi = input("Ingin mencari lagi? (y/n): ").lower()
        if lagi != 'y':
            break

if __name__ == "__main__":
    main()

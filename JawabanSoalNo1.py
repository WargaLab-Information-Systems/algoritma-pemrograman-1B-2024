def data_karyawan ():
    karyawan_list = []
    for i in range(5):
      print(f"masukkan data karyawan ke- {i+1}:")
      NIP = input("masukkan NIP: ")
      nama = input("masukkan nama: ")
      alamat = input("masukkan alamat: ")
      departemen = input("masukkan departemen:")
      jabatan = input("masukkan jabatan: ")

      karyawan_list.append([NIP, nama, alamat, departemen, jabatan])
      print()
    return karyawan_list

def mencari_karyawan(karyawan_list, search):
    hasil = []
    for karyawan in karyawan_list:
      for data in karyawan:
        if search in data:
          hasil.append(karyawan)
          break
    return hasil

def tampilkan_hasil_mencari(hasil):
    print("-"*50)
    if hasil:
      print("\hasil pencarian:")
      for karyawan in hasil:
        print(f"NIP: {karyawan[0]}, nama: {karyawan[1]}, alamat: {karyawan[2]}, departemen: {karyawan[3]}, jabatan: {karyawan[4]}")
    else:
      print("data tidak ditemukan")

def main():
    print("program pencarian data")
    karyawan_list = data_karyawan()

    while True:

      search = input("masukkan nilai pencarian: ")

      hasil = mencari_karyawan(karyawan_list, search)
      tampilkan_hasil_mencari(hasil)

      ask = input("apakah ingin melanjutkan pencarian (y/n): ")
      if ask != "y":
        print("program selesai")
        break

if __name__ == "__main__":
  main()
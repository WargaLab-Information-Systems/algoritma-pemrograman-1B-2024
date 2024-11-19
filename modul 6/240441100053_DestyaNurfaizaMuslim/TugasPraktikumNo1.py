# List untuk menyimpan data karyawan
karyawan = []

# Menginputkan minimal 5 data karyawan
def tambah_karyawan():
    while True:
        print(f"Masukkan Data Karyawan (ke-{len(karyawan) + 1}): ")
        nip = input("NIP : ")
        nama = input("Nama : ")
        alamat = input("Alamat : ")
        dept = input("Departemen : ")
        jbtn = input("Jabatan : ")
        print()

        karyawan.append([nip, nama, alamat, dept, jbtn])

        if len(karyawan) >= 5:
            ulang = input("Apakah anda ingin memasukkan data lagi (y/n) : ")
            if ulang != "y":
                print("Data Karyawan telah ditambahkan")
                print()
                break
    return karyawan

# Mencari data karyawan dan menampilkan semua data karyawan berdasarkan atribut yang dicari
def cari_karyawan():
    print()
    print("Pencarian Data Karyawan")
    print("Cari Berdasarkan : ")
    print("1. NIP")
    print("2. Nama")
    print("3. Alamat")
    print("4. Departemen")
    print("5. Jabatan")
    
    pilih = input("Masukkan atribut pencarian anda (1/2/3/4/5) : ")
    cari = input("Masukkan data karyawan yang anda cari : ")

    pencarian = []

    if pilih == "1":
        pencarian = [data for data in karyawan if cari in data[0]]  
    elif pilih == "2":
        pencarian = [data for data in karyawan if cari in data[1]] 
    elif pilih == "3":
        pencarian = [data for data in karyawan if cari in data[2]] 
    elif pilih == "4":
        pencarian = [data for data in karyawan if cari in data[3]] 
    elif pilih == "5":
        pencarian = [data for data in karyawan if cari in data[4]]  
    else:
        print("Pilihan anda salah")

    # Menampilkan data karyawan yang ditemukan
    if pencarian:
        print()
        print("Hasil Pencarian")
        for data in pencarian:
            print(f"NIP: {data[0]}, Nama: {data[1]}, Alamat: {data[2]}, Departemen: {data[3]}, Jabatan: {data[4]}")
    else:
        print("Data karyawan tidak ditemukan dalam program")

# Memilih fitur pada program
def menu():
    while True:
        pilih = input('''
            Program Pendataan Karyawan Perusahaan 
                     
                1. Menambahkan Data Karyawan 
                2. Pencarian Data Karyawan   
                3. Keluar
                     
            Masukkan Menu Berdasarkan Kebutuhan (1-3) : ''')

        if pilih == "1":
            tambah_karyawan()
        elif pilih == "2":
            cari_karyawan()
        elif pilih == "3":
            print("Keluar dari Program")
            break
        else:
            print("Inputan anda salah")

menu()
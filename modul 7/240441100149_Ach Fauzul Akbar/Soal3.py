data_siswa = {}

def tambah_data():
    nama = input('masukkan nama siswa: ')
    asal_sekolah = input('masukkan asal sekolah: ')
    kelas = input('masukkan kelompok kelas: ')

    if kelas not in data_siswa:
        data_siswa[kelas] = []

    if len(data_siswa[kelas]) < 3:
        data_siswa[kelas].append({'nama': nama, 'asal_sekolah': asal_sekolah})
        print(f'siswa {nama} telah terdaftar di kelas {kelas}')
    else:
        print(f'Kelas {kelas} sudah penuh')

def tampil_data():
    if not data_siswa:
        print('siswa belum terdaftar')
        return

    for kelas, siswa_list in data_siswa.items():
        for siswa in siswa_list:
            print(f'nama: {siswa["nama"]}, asal sekolah: {siswa["asal_sekolah"]}, kelas: {kelas}')

def update():
    nama = input('masukkan nama siswa yang ingin diubah: ')
    for kelas, siswa_list in data_siswa.items():
        for siswa in siswa_list:
            if siswa['nama'] == nama:
                nama_baru = input('masukkan nama baru: ')
                asal_sekolah_baru = input('masukkan asal sekolah yang baru: ')
                siswa['nama'] = nama_baru
                siswa['asal_sekolah'] = asal_sekolah_baru
                print('data berhasil diperbarui')
                return
    print('siswa tidak terdaftar')

def delete():
    nama = input('masukkan nama siswa yang ingin dihapus: ')
    for kelas, siswa_list in data_siswa.items():
        for siswa in siswa_list:
            if siswa['nama'] == nama:
                siswa_list.remove(siswa)
                print('nama terhapus')
                return
    print('nama tidak terdaftar')

def main():
    while True:
        print('---pilih data---')
        print('1 tambah data')
        print('2 tampilkan data')
        print('3 ubah data')
        print('4 hapus data')
        print('5 keluar')

        pilih = input('pilih data 1/2/3/4/5: ')

        if pilih == '1':
            tambah_data()
        elif pilih == '2':
            tampil_data()
        elif pilih == '3':
            update()
        elif pilih == '4':
            delete()
        elif pilih == '5':
            break
        else:
            print('Pilihan tidak valid')

main()

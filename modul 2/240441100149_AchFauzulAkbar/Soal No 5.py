nama = input('masukan nama anda ! ')
umur = int(input('berapa umur anda ? '))
kartu_member = input('apakah anda memiliki kartu_member ? [y/n]: ')
total_belanja = int(input('berapa total belanja anda ? '))
diskon = 0

if umur < 18:
    print('anda masih dibawah umur')
    exit()

else:
    if kartu_member == 'y':
        diskon += 15
    if total_belanja >= 500000 :
        diskon += 10
# rumus harga setelah diskon
total_diskon = (diskon / 100) * total_belanja
total_setelah_diskon = total_belanja - total_diskon

# hasil
print(f'{nama}, anda mendapatkan diskon sebesar {diskon}%, harga awal sebesar Rp {total_belanja}, harga setelah diskon sebesar Rp {total_setelah_diskon}')

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
        diskon += 0.15
    elif total_belanja >= 500000 :
        diskon += 0.10
# rumus harga setelah diskon
hargadiskon = int(total_belanja * (1 - diskon))


# hasil
print(f'{nama}, anda mendapatkan diskon sebesar {diskon}, harga awal sebesar {total_belanja} Rp, menjadi {hargadiskon} Rp')

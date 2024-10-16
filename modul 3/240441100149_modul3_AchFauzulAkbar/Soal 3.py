while True:
    lama_menyewa = int(input('masukan lama sewa DVD : '))
    #hitung keterlambatan
    hari_terlambat = lama_menyewa - 5
    
    denda_harian = 2500
    denda_tambahan = 5500
    total_denda_denda = 0
    
    if lama_menyewa >5 :
        total_denda = denda_harian * hari_terlambat
    print(total_denda)

    if hari_terlambat >10:
        denda_tambahan = (hari_terlambat - 10 // 5)*denda_tambahan
        total_denda_denda += denda_tambahan
    print(f'total denda anda adala : Rp {total_denda}')

    tanyaminjam = input('apakah anda ingin meminjam lagi [ya/tidak]?')
    if tanyaminjam != 'ya':
        break


while True:
    lama_menyewa = int(input('masukan lama sewa DVD : '))
    hari_terlambat = 0
    denda_harian = 2500
    denda_tambahan = 5500
    total_denda_denda = 0
    hari_terlambat = int(input('berapa lama keterlambatan anda? '))
    if hari_terlambat >5 :
        total_denda = denda_harian * hari_terlambat
    print(total_denda)

    if hari_terlambat >10:
        denda_tambahan = (hari_terlambat  // 5)*denda_tambahan
        total_denda_denda += denda_tambahan
    print(f'total denda anda adala : Rp {total_denda}')

    tanyaminjam = input('apakah anda ingin meminjam lagi [ya/tidak]?')
    if tanyaminjam != 'ya':
        break


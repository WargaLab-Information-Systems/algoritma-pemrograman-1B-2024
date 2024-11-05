def calculate_discount(total_belanja, jenis_keanggotaan):
    diskon = 0
#cek apakah ada keanggotaan jg hitung buat diskon anggota
    if jenis_keanggotaan == "Gold":
        diskon = 0.15
    elif jenis_keanggotaan == "Silver":
        diskon = 0.10
    elif jenis_keanggotaan == "Bronze":
        diskon = 0.05
    else:
        diskon = 0
#cek belanja>1 jt
    if total_belanja > 1000000:
        diskon += 0.05

    totaldiskon = total_belanja * diskon
    return totaldiskon

total_belanja = float(input("Masukan total belanja: "))
if total_belanja <= 500:
    print("masukkan total belanja lebih dari 500")
else:
    jenis_keanggotaan = input("Masukan jenis keanggotaan (Gold/Silver/Bronze/Tidak Punya): ")
    diskon = calculate_discount(total_belanja, jenis_keanggotaan)
    print(f"Diskon yang didapat: Rp {diskon}")

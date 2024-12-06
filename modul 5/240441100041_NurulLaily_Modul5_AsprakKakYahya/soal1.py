def calculate_discount(total_belanja, keanggotaan):
    if keanggotaan.lower() == "gold":
        diskon = 0.15
    elif keanggotaan.lower() == "silver":
        diskon = 0.10
    elif keanggotaan.lower() == "bronze":
        diskon = 0.05
    else:
        diskon = 0.0

    potongan_awal = total_belanja * diskon

    if total_belanja > 1000000:
        potongan_tambahan = total_belanja * 0.05
    else:
        potongan_tambahan = 0

    total_potongan = potongan_awal + potongan_tambahan

    total_bayar = total_belanja - total_potongan

    return total_bayar, total_potongan


total_belanja = float(input("Masukkan total belanja: "))
keanggotaan = input("Masukkan jenis keanggotaan (Gold, Silver, Bronze, atau Tidak ada): ")

if total_belanja < 1:
    print("Total belanja tidak valid,Silahkan masukkan lagi")
else:
    total_bayar, total_potongan = calculate_discount(total_belanja, keanggotaan)
    print(f"Total Potongan: Rp {total_potongan}")
    print(f"Total Bayar: Rp {total_bayar}")
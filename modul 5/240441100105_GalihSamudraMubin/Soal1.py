def calculate_discount(total_belanja, keanggotaan):
    if keanggotaan == "gold":
        diskon_keanggotaan = 15
    elif keanggotaan == "silver":
        diskon_keanggotaan = 10
    elif keanggotaan == "bronze":
        diskon_keanggotaan = 5
    else:
        diskon_keanggotaan = 0

    if total_belanja >= 1000000:
        diskon_tambahan = 5
    else:
        diskon_tambahan = 0 

    total_diskon_keanggotaan = total_belanja * (diskon_keanggotaan / 100)
    total_diskon_tambahan = total_belanja * (diskon_tambahan / 100)
    total_diskon = total_diskon_keanggotaan + total_diskon_tambahan
    total_setelah_diskon = total_belanja - total_diskon
    
    return total_setelah_diskon,keanggotaan, diskon_keanggotaan, diskon_tambahan, total_diskon_keanggotaan, total_diskon_tambahan, total_diskon

total_belanja = float(input("Masukkan total belanja: "))
keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak ada): ").lower()

total_setelah_diskon,keanggotaan, diskon_keanggotaan, diskon_tambahan, total_diskon_keanggotaan, total_diskon_tambahan, total_diskon = calculate_discount(total_belanja, keanggotaan)

print("\n------------- Nota Belanja -------------")
print(f"Total Belanja Awal       : Rp{total_belanja:,.2f}")
print(f"Status Keanggotaan       : {keanggotaan}")
print(f"Diskon Keanggotaan       : {diskon_keanggotaan}%")
print(f"Total Diskon Keanggotaan : Rp{total_diskon_keanggotaan:,.2f}")
print(f"Diskon Tambahan          : {diskon_tambahan}%")
print(f"Total Diskon Tambahan    : Rp{total_diskon_tambahan:,.2f}")
print(f"Total Diskon Keseluruhan : Rp{total_diskon:,.2f}")
print(f"Total Setelah Diskon     : Rp{total_setelah_diskon:,.2f}")
print("----------------------------------------")

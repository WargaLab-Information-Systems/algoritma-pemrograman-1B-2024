def calculate_discount():
    belanja = int(input("Masukkan total belanja: "))
    member = input("Apa keanggotaan anda (gold/silver/bronze/tidak ada): ").lower()
    
    if member == "gold":
        diskon_keanggotaan = 15
    elif member == "silver":
        diskon_keanggotaan = 10
    elif member == "bronze":
        diskon_keanggotaan = 5
    else:
        diskon_keanggotaan = 0

    diskon_tambahan = 0
    if belanja > 1000000:
        diskon_tambahan = 5

    total_diskon_persen = diskon_keanggotaan + diskon_tambahan
    total_diskon = int(belanja * total_diskon_persen / 100)
    total_bayar = int(belanja - total_diskon)
    
    print("Diskon yang didapat:", total_diskon_persen, "%")
    print("Total Diskon: Rp", total_diskon)
    print("Harga Setelah Diskon: Rp", total_bayar)
    
    return total_bayar

print(calculate_discount())
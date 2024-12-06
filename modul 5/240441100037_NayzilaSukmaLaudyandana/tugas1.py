def calculate_discount(total, anggota):
    anggota = anggota
    if anggota == "gold":
        diskon = 0.15
    elif anggota == "silver":
        diskon = 0.10
    elif anggota == "bronze":
        diskon = 0.05
    else:
        diskon = 0.0

    if total > 1000000:
        diskon += 0.05

    tl_diskon = total * diskon
    harga = total - tl_diskon

    return harga, tl_diskon


while True:
        total = int(input("Total Belanja: "))
        if total > 1:
            break
        else:
            print("Total belanja harus lebih dari 1!!!")
anggota = input("Masukkan Level Keanggotaan: ") 
harga, tl_diskon = calculate_discount(total, anggota)

print("Total diskon: Rp.",tl_diskon)
print("Harga setelah diskon: Rp.",harga)
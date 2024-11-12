def calculate_discount(total_belanja, membership):
    if membership == "gold":
        discount = 0.15
    elif membership == "silver":
        discount = 0.10
    elif membership == "bronze":
        discount = 0.05
    else:
        discount = 0

    if total_belanja > 1000000:
        discount += 0.05

    # Menghitung total setelah diskon
    total_diskon = total_belanja * discount
    total_setelah_diskon = total_belanja - total_diskon
    # print("Total setelah diskon:", total_setelah_diskon)
    return total_setelah_diskon

total_belanja = float(input("Masukkan total belanja: "))
membership = input("Masukkan jenis keanggotaan (gold/silver/bronze/gapunya): ")

calculate_discount(total_belanja, membership)
# total_setelah_diskon = calculate_discount(total_belanja, membership)
# print("Total setelah diskon:", total_setelah_diskon)

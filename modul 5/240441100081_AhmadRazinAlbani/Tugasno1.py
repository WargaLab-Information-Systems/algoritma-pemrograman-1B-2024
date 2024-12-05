total_belanja = int(input("Masukkan total belanja anda: "))
jenis_keanggotaan = input("Masukkan jenis keanggotaan anda(gold/silver/bronze)/n: ")
diskon = 0
def calculate_discount(total_belanja, jenis_keanggotaan, diskon):
    if jenis_keanggotaan == "gold":
        diskon += 15/100
    elif jenis_keanggotaan == "silver":
        diskon += 10/100
    elif jenis_keanggotaan == "bronze":
        diskon += 5/100
    if total_belanja > 1000000:
        diskon += 5/100
    total_diskon = total_belanja * diskon
    harga_setelah_diskon = total_belanja - total_diskon
    return total_diskon, harga_setelah_diskon
total_diskon, harga_setelah_diskon = calculate_discount(total_belanja, jenis_keanggotaan, diskon)

print(f"Total belanja anda: {total_belanja} ")
print(f"Total diskon yang didapat: {total_diskon} ")
print(f"Total belanja anda setelah diskon: {harga_setelah_diskon}")


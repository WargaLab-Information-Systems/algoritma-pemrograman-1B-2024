def calculate_discount(total_belanja, keanggotaan):
    # Diskon awal berdasarkan jenis keanggotaan
    if keanggotaan == "GOLD":
        diskon = 0.15
    elif keanggotaan == "SILVER":
        diskon = 0.10
    elif keanggotaan == "BRONZE":
        diskon = 0.05
    else:
        diskon = 0.0
    
    diskon_akhir = total_belanja * diskon
    
    if total_belanja > 1000000:
        tambahan_diskon = total_belanja * 0.05
        diskon_akhir += tambahan_diskon
    
    total_setelah_diskon = total_belanja - diskon_akhir
    
    return total_setelah_diskon

try:
    total_belanja = float(input("Masukkan total belanja : "))
    keanggotaan = input("Masukkan jenis keanggotaan (gold, silver, bronze, atau none) : ").upper()
    total_setelah_diskon = calculate_discount(total_belanja, keanggotaan)
    print("Total setelah diskon:", total_setelah_diskon)
except ValueError:
    print("Input tidak valid. Pastikan Anda memasukkan angka untuk total belanja.")


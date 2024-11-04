total_belanja = int(input("Masukkan total belanja: "))
cek_keanggotaan = input("Apakah anda memiliki kartu keanggotaan? (ya/tidak):")
keanggotaan = None # nilai default

if cek_keanggotaan == 'ya':
    while True:
        keanggotaan = input("Masukkan keanggotaan (gold/silver/bronze):") 
        if keanggotaan == "gold" or keanggotaan == "silver" or keanggotaan == "bronze":
            break
        else:
            print("Masukkan keanggotaan yang sesuai")
    
def calculate_discount(total_belanja, keanggotaan):
    if keanggotaan == "gold":
        diskon = 15  
    elif keanggotaan == "silver":
        diskon = 10  
    elif keanggotaan == "bronze":
        diskon = 5  
    else:
        diskon = 0  

    if total_belanja >= 1000000:
        diskon += 5  

    total_diskon = total_belanja * (diskon/100) # total diskon
    harga_akhir = total_belanja - total_diskon # harga after diskon

    return harga_akhir

harga_setelah_diskon = calculate_discount(total_belanja, keanggotaan)

print("Harga setelah diskon:", harga_setelah_diskon)

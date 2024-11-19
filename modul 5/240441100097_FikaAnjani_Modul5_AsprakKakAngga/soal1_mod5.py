def calculate_discount(total_belanja, kartu_member):
    
    if kartu_member == 'gold':
        print("Selamat anda mendapatkan diskon 15%")
        diskon = 15
    elif kartu_member == 'silver':
        print("Selamat anda mendapatkan diskon 10%")
        diskon = 10
    elif kartu_member == 'bronze':
        print("Selamat anda mendapatkan diskon 5%")
        diskon = 5
    else:
        print("Ayo daftarkan diri anda dan dapatkan diskon anda")
        diskon = 0  

    if total_belanja > 1000000:
        print("Selamat anda mendapatkan diskon 5%")
        diskon += 5

    total_diskon = total_belanja * (diskon / 100)
    total_setelah_diskon = total_belanja - total_diskon
    
    return total_diskon, total_setelah_diskon

total_belanja = int(input("Masukkan total belanja: ")) 
kartu_member = input("Masukkan jenis kartu member (gold/silver/bronze): ")  

total_diskon, total_setelah_diskon = calculate_discount(total_belanja, kartu_member)

print("Total diskon:", total_diskon)
print("Total setelah diskon:", total_setelah_diskon) 
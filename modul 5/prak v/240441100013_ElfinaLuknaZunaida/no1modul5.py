def calculate_discount(total_belanja, keanggotaan):
    diskon = 0


    if keanggotaan == "Gold":
        diskon = 15
    elif keanggotaan == "Silver":
        diskon = 10
    elif keanggotaan == "Bronze":
        diskon = 5
    else:
        diskon = 0  
    

    if total_belanja > 1000000:
        diskon += 5
    
    total_diskon = (diskon / 100) * total_belanja
    return total_diskon

total_belanja = float(input("Masukkan total belanja: "))
keanggotaan = input("Masukkan jenis keanggotaan: ")

# Menghitung diskon
# diskon = calculate_discount(total_belanja, keanggotaan)
print("Diskon yang didapat: ", calculate_discount(total_belanja, keanggotaan))
print(f"Total belanja :{total_belanja - calculate_discount(total_belanja, keanggotaan)}")

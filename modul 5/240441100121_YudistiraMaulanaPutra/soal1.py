def calculate_discount(totalBelanja, jenisKeanggotaan):
    diskon = 0
    if jenisKeanggotaan == "gold":
        diskon = 0.15
    elif jenisKeanggotaan == "silver":
        diskon = 0.10
    elif jenisKeanggotaan == "bronze":
        diskon = 0.05
    else:
        diskon = 0
    if  totalBelanja > 1000000:
        diskon += 0.05
    diskonDiDapat = totalBelanja * diskon 
    totalDiskon = totalBelanja - diskonDiDapat 
    return diskonDiDapat, totalDiskon
jenisKeanggotaan = str(input("Masukkan keanggotaan: "))
totalBelanja = int(input("Masukkan total belanja: "))
diskon, setelahDiskon = calculate_discount(totalBelanja, jenisKeanggotaan)
print(f"Total belanja: {totalBelanja}")
print(f"Diskon didapat: {diskon}")
print(f"Total belanja setelah diskon: {setelahDiskon}")
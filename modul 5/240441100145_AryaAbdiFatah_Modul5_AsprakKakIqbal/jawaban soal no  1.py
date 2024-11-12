def kalkulator_diskon(anggota, totalBelanja):
    diskon = 0
    if anggota == "gold":
        diskon = 15 
    elif anggota == "silver":
        diskon = 10
    elif anggota == "bronze":
        diskon = 5 
    else:
        diskon = 0
        
    if totalBelanja > 1000000:
        diskon += 5   
    return diskon 
        
keanggotaan = input("Apakah anda memiliki keanggotaan?(y/n)").lower()
if keanggotaan == "y":
    anggota = input("Masukkan jenis keanggotaan anda: ").lower()
else:
    keanggotaan == "n"
    print("Anda tidak mendapatkan diskon member")
    anggota = ""


totalBelanja = int(input("Masukkan total belanja anda: "))

diskon = kalkulator_diskon(anggota, totalBelanja)
totalDiskon = (diskon / 100) * totalBelanja
totalSetelahDiskon = totalBelanja - totalDiskon

print("=================================================")
print(f"Anda mendapatkan diskon sebesar {diskon}%")
print(f"Total harga diskonnya adalah Rp.{totalDiskon}")
print(f"Total harga setelah diskon adalah Rp.{totalSetelahDiskon}")
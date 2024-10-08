nama = input("Masukkan nama pembeli: ")
total_belanja = int(input("Masukkan total belanja (Rp): "))
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ")
usia = int(input("Masukkan usia pembeli: "))

diskon = 0

if usia < 18:
    print("Maaf, usia anda belum mencukupi")
    exit()
    
if member == "ya":
    diskon += 15  
        
if total_belanja > 500000:
    diskon += 10      

total_diskon = total_belanja * (diskon/100)
total_setelah_diskon = total_belanja - total_diskon

print(f"Nama Pembeli: {nama}")
print(f"Diskon yang didapatkan: {diskon}%")
print(f"Total harga sebelum diskon: Rp{total_belanja}")
print(f"Total harga setelah diskon: Rp{total_setelah_diskon}")

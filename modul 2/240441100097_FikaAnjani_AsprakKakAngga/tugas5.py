nama = input("Masukkan nama:")
umur = int(input("Masukkan usia:"))

if umur < 18:
    print("umur anda tidak mencukupi")
    exit()
else:
    total_belanja = int(input("Masukkan total belanja: Rp"))

    kartu_member = input("Apakah anda memiliki kartu member? (ya/tidak): ")

    diskon = 0

    if kartu_member == "ya":
        diskon += 15
    if total_belanja >= 500000:
        diskon += 10
        
total_diskon= total_belanja*diskon/100
total_harga_setelah_diskon= int(total_belanja-total_diskon)

print(f"\nnama:{nama}")
print(f"anda mendapat diskon: {diskon}%")
print(f"Total harga sebelum diskon : Rp{total_belanja}")
print(f"Total harga setelah diskon : Rp{total_harga_setelah_diskon}")
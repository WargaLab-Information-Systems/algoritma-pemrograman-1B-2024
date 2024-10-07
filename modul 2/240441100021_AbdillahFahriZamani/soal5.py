# Input
nama = input("Masukkan nama: ")
usia = int(input("Masukkan usia anda: "))

# Penyeleksian
if usia < 18:
    print("Maaf usia anda belum mencukupi")
else:
    member = input("Apakah anda memiliki kartu member? (iya/tidak): ")
    total_pesanan = float(input("Berapa total pesanan anda? : "))

    # Inisialisasi diskon
    diskon_member = 15 if member == "iya" else 0
    diskon_total_pesanan = 10 if total_pesanan > 500000 else 0

    # Penghitungan total diskon
    total_diskon = diskon_member + diskon_total_pesanan
    total_setelah_diskon = (total_diskon / 100) * total_pesanan
    sebelum_diskon = total_pesanan
    sesudah_diskon = total_pesanan - total_setelah_diskon

    # Output
    print(f"\n Nama anda: {nama}")
    print(f"Diskon member {diskon_member}%.")
    print(f"Diskon total pesanan {diskon_total_pesanan}%.")
    print(f"Total diskon anda: {total_diskon}%.")
    print(f"Harga sebelum diskon: Rp{sebelum_diskon:.2f}")
    print(f"Harga setelah diskon: Rp{sesudah_diskon:.2f}")

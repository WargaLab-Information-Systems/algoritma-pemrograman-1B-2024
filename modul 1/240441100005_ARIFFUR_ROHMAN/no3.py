# usd 35 kurs 15.219
jumlah_usd = float(input("Masukkan jumlah uang dalam USD: "))
kurs_usd_to_idr = float(input("Masukkan nilai tukar USD ke IDR: "))

jumlah_idr = jumlah_usd * kurs_usd_to_idr

print(f"Jumlah uang dalam Rupiah: Rp {jumlah_idr:,}")

total_gaji_reguler = 100000 * 7  # Gaji reguler per minggu
total_jam_lembur_mingguan = 0
total_gaji_lembur = 0

for hari in range(1, 8):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari}: "))

    # Jika lembur melebihi batas per hari
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0
    # Jika total lembur mingguan mencapai atau melebihi 40 jam
    if total_jam_lembur_mingguan + jam_lembur >= 40:
        print("Total lembur mencapai batas mingguan, lembur dihentikan.")
        jam_lembur = 40 - total_jam_lembur_mingguan  # Hanya tambahkan yang tersisa hingga 40 jam

    # Hitung gaji lembur berdasarkan jam lembur harian
    if jam_lembur == 0:
        gaji_lembur_harian = 0
    elif jam_lembur < 4:
        gaji_lembur_harian = jam_lembur * 25000
    elif jam_lembur >= 4:
        gaji_lembur_harian = 100000
    elif jam_lembur >= 6:
        gaji_lembur_harian = 200000
    elif jam_lembur >= 8:
        gaji_lembur_harian = 300000

    # Tambahkan jam lembur dan gaji lembur harian ke total
    total_jam_lembur_mingguan += jam_lembur
    total_gaji_lembur += gaji_lembur_harian

    print(f"Lembur hari ke-{hari}: {jam_lembur} jam, Gaji lembur: Rp{gaji_lembur_harian}")

# Total gaji mingguan termasuk lembur
total_gaji_mingguan = total_gaji_reguler + total_gaji_lembur

# Cetak hasil akhir
print("\nTotal lembur selama satu minggu:", total_jam_lembur_mingguan, "jam")
print(f"Total gaji lembur selama satu minggu: Rp", total_gaji_lembur)
print(f"Total gaji mingguan tanpa lembur: Rp", total_gaji_reguler)
print(f"Total gaji mingguan termasuk lembur: Rp", total_gaji_mingguan)
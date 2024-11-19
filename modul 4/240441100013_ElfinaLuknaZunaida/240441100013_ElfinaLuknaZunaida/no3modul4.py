gaji_harian = 100000  # Gaji per hari
maks_lembur_harian = 8  # Maksimal jam lembur per hari
maks_lembur_mingguan = 40  # Maksimal jam lembur per minggu
total_gaji_satu_minggu = 0
total_lembur_mingguan = 0
total_gaji_lembur = 0

for hari in range(1, 8):
    # Input jam lembur harian
    jam_lembur = int(input(f"Masukkan jam lembur untuk hari ke-{hari}: "))

    total_gaji_satu_minggu += gaji_harian

    if total_lembur_mingguan > maks_lembur_mingguan:
        print("Lembur dihentikan. Total lembur mingguan sudah mencapai batas.")
        continue  

    # batasi jam lembur per hari 
    if jam_lembur > maks_lembur_harian:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0

    # Hitung gaji lembur 
    if jam_lembur >= 8:
        gaji_lembur = 300000
    elif jam_lembur >= 6:
        gaji_lembur = 200000
    elif jam_lembur >= 4:
        gaji_lembur = 100000
    elif jam_lembur > 0:
        gaji_lembur = jam_lembur * 25000
    else:
        gaji_lembur = 0  

    total_lembur_mingguan += jam_lembur
    total_gaji_lembur += gaji_lembur

# Total gaji mingguan
total_gaji_mingguan = total_gaji_satu_minggu + total_gaji_lembur

# hasil
print(f"Total lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total gaji lembur selama satu minggu: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_satu_minggu}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")

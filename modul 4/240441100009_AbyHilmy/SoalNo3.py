# Konstanta
gaji_harian = 100000
jam_max_lembur = 8
lembur_limit_mingguan = 40
bonus_lembur = {0: 0, 1: 25000, 2: 25000, 3: 25000, 4: 100000,5: 100000, 6: 200000,7: 200000, 8: 300000}

# Variabel untuk menghitung total
total_gaji_lembur = 0
total_lembur_mingguan = 0
total_gaji_mingguan = 0

# Input jam lembur per hari selama 7 hari
jam_lembur_harian = []
for i in range(7):
    jam_lembur = int(input(f"Masukkan jam lembur untuk hari ke-{i+1}: "))
    
    # Validasi lembur
    if jam_lembur > jam_max_lembur:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = jam_max_lembur  # Hanya ambil maksimum 8 jam untuk perhitungan

    total_lembur_mingguan += jam_lembur

    # Hitung gaji lembur
    if total_lembur_mingguan > lembur_limit_mingguan:
        print("Lembur mingguan sudah mencapai batas, tidak dihitung.")
        jam_lembur = 0  # Tidak ada lembur yang dihitung
    
    if jam_lembur > 0:
        gaji_lembur = bonus_lembur[jam_lembur]
    else:
        gaji_lembur = 0

    total_gaji_lembur += gaji_lembur
    jam_lembur_harian += [jam_lembur]

# Hitung total gaji mingguan
total_gaji_mingguan = gaji_harian * 7 + total_gaji_lembur

# Output hasil
print("\nLembur per hari:", jam_lembur_harian)
print("Total lembur selama satu minggu:", total_lembur_mingguan)
print("Total gaji lembur:", total_gaji_lembur)
print("Total gaji mingguan tanpa lembur:", gaji_harian * 7)
print("Total gaji mingguan termasuk lembur:", total_gaji_mingguan)

gaji_harian = 100000

jam_lembur_per_hari = []
for i in range(7):
    jam = int(input(f"Jam lembur hari ke-{i+1}: "))
    jam_lembur_per_hari.append(jam)

total_lembur = sum(min(lembur, 8) for lembur in jam_lembur_per_hari)
total_gaji_lembur = 0

if total_lembur < 40:
    for lembur in jam_lembur_per_hari:
        if lembur == 0:
            continue
        elif lembur < 4:
            total_gaji_lembur += lembur * 25000
        elif lembur == 4:
            total_gaji_lembur += 100000
        elif lembur == 6:
            total_gaji_lembur += 200000
        elif lembur == 8:
            total_gaji_lembur += 300000

total_gaji = (gaji_harian * 7) + total_gaji_lembur

print(f"Lembur total: {total_lembur} jam")
print(f"Gaji lembur: Rp{total_gaji_lembur}")
print(f"Gaji mingguan total: Rp{total_gaji}")




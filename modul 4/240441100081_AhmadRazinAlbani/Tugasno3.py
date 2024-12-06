gaji_harian = 100000
total_gaji_reguler = gaji_harian * 7
total_lembur = 0
total_jam_lembur = 0

# Input jam lembur per hari selama 7 hari
jam_lembur_per_hari = []
for i in range(7):
    jam = int(input(f"Masukkan jam lembur untuk hari ke-{i+1}: "))
    jam_lembur_per_hari += [jam]

# Proses perhitungan gaji lembur
for jam_lembur in jam_lembur_per_hari:
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 8  
    total_jam_lembur += jam_lembur
    
    if total_jam_lembur >= 40:
        print("Total jam lembur dalam seminggu sudah mencapai batas maksimum.")
        break
    
    if jam_lembur == 0:
        continue
    elif 1 <= jam_lembur <= 3:
        total_lembur += jam_lembur * 25000
    elif jam_lembur == 4:
        total_lembur += 100000
    elif jam_lembur == 6:
        total_lembur += 200000
    elif jam_lembur == 8:
        total_lembur += 300000

# Hitung total gaji mingguan
total_gaji_mingguan = total_gaji_reguler + total_lembur

# hasil
print(f"Total jam lembur selama satu minggu: {total_jam_lembur} jam")
print(f"Total gaji lembur: Rp{total_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_reguler}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")



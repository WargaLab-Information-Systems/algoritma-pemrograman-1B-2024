gaji_harian = 100000
gaji_lembur = 0
total_lembur = 0
jam_lembur_total = 0

# Loop untuk menghitung lembur setiap hari selama 7 hari
for hari in range(1, 8):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari}: "))
    
    # Jika lembur melebihi batas 8 jam
    if jam_lembur > 8:
        jam_lembur = 8
        print("Lembur melebihi batas, tidak dihitung.")
    
    # Tambahkan ke total lembur mingguan
    jam_lembur_total += jam_lembur
    
    # Jika total lembur mingguan mencapai atau melebihi 40 jam
    if jam_lembur_total >= 40:
        print("Total lembur mencapai batas mingguan.")
        jam_lembur_total = 40
        break

    # Hitung bonus lembur
    if jam_lembur == 0:
        bonus = 0
    elif jam_lembur <= 3:
        bonus = jam_lembur * 25000
    elif jam_lembur == 4:
        bonus = 100000
    elif jam_lembur == 6:
        bonus = 200000
    elif jam_lembur == 8:
        bonus = 300000
    
        

# Tambahkan bonus lembur ke total gaji lembur
gaji_lembur += bonus

# Total gaji reguler selama 7 hari
gaji_mingguan_reguler = gaji_harian * 7

# Total gaji mingguan dengan lembur
total_gaji_mingguan = gaji_mingguan_reguler + gaji_lembur

# Output hasil
print(f"Total jam lembur selama seminggu: {jam_lembur_total}")
print(f"Total gaji lembur: Rp{gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{gaji_mingguan_reguler}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")
gaji_harian = 100000
tambahan_lembur = 0
total_gaji_lembur = 0
total_lembur_mingguan = 0
total_gaji_mingguan = 0
total_gaji_mingguan_tanpa_lembur = gaji_harian * 7

for hari in range(7):
    jam_lembur = int(input(f"Masukkan jam lembur untuk hari ke-{hari + 1}: "))
    
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0  
    total_lembur_mingguan += jam_lembur
    if total_lembur_mingguan >= 40:
        print("Total jam lembur sudah mencapai batas maksimal dalam seminggu, lembur dihentikan.")
        break
    total_lembur_mingguan += jam_lembur

    if jam_lembur == 0:
        tambahan_lembur = 0
    elif 1 <= jam_lembur <= 3:
        tambahan_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        tambahan_lembur = 100000
    elif jam_lembur == 6:
        tambahan_lembur = 200000
    elif jam_lembur == 8:
        tambahan_lembur = 300000
    else: 
        tambahan_lembur =jam_lembur * 25000
    
    total_gaji_lembur += tambahan_lembur
    print(f"Lembur hari ke-{hari + 1}: {jam_lembur} jam, Tambahan lembur: Rp{tambahan_lembur}")

total_gaji_mingguan = total_gaji_mingguan_tanpa_lembur + total_gaji_lembur

print(f"\nTotal lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_mingguan_tanpa_lembur}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")
gaji_harian = 100000
jam_kerja_per_hari = 12
max_jam_lembur_harian = 8
max_jam_lembur_mingguan = 40
tambahan_per_jam = 25000

total_gaji_reguler_mingguan = gaji_harian * 7
total_jam_lembur_mingguan = 0
total_gaji_lembur_mingguan = 0

print("Masukkan jam lembur harian untuk 7 hari berturut-turut:")

for hari in range(1, 8):
    jam_lembur = int(input(f"Jam lembur hari ke-{hari}: "))
    
    if jam_lembur > max_jam_lembur_harian:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur_dihitung = max_jam_lembur_harian  
    else:
        jam_lembur_dihitung = jam_lembur  
    
    gaji_lembur_harian = 0  
    if total_jam_lembur_mingguan < max_jam_lembur_mingguan:
        if total_jam_lembur_mingguan + jam_lembur_dihitung > max_jam_lembur_mingguan:
            jam_lembur_dihitung = max_jam_lembur_mingguan - total_jam_lembur_mingguan
        total_jam_lembur_mingguan += jam_lembur_dihitung
        
        if jam_lembur_dihitung == 8:
            gaji_lembur_harian = 300000
        elif jam_lembur_dihitung == 6:
            gaji_lembur_harian = 200000
        elif jam_lembur_dihitung == 4:
            gaji_lembur_harian = 100000
        elif jam_lembur_dihitung == 5:
            gaji_lembur_harian = 100000 + 50000  # 4 jam + Rp50.000
        elif jam_lembur_dihitung == 7:
            gaji_lembur_harian = 200000 + 50000  # 6 jam + Rp50.000
        elif 1 <= jam_lembur_dihitung < 4:
            gaji_lembur_harian = tambahan_per_jam * jam_lembur_dihitung
        
        total_gaji_lembur_mingguan += gaji_lembur_harian
    else:
        print("Total lembur mingguan mencapai batas, lembur dihentikan.")
        break
    
    print(f"Gaji lembur hari ke-{hari}: Rp {gaji_lembur_harian}")

total_gaji_mingguan_dengan_lembur = total_gaji_reguler_mingguan + total_gaji_lembur_mingguan

print("\n=== Rincian Gaji Mingguan Mas Ironi ===")
print("Total jam lembur selama seminggu:", total_jam_lembur_mingguan)
print("Total gaji lembur mingguan: Rp", total_gaji_lembur_mingguan)
print("Total gaji mingguan tanpa lembur: Rp", total_gaji_reguler_mingguan)
print("Total gaji mingguan termasuk lembur: Rp", total_gaji_mingguan_dengan_lembur)

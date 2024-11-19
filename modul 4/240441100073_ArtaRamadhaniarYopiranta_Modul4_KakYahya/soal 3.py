Gaji_harian = 100000
Maks_lembur = 8
Maks_lembur_mingguan = 40
total_gaji = 0
total_lembur = 0
total_gaji_lembur = 0

for hari in range(1, 8):
    jam_lembur = int(input(f"Masukkan jam lembur untuk hari ke-{hari}: "))
    
    if jam_lembur > Maks_lembur:
        print("Lembur melebihi batas, tidak dihitung.")
        continue
    
    total_lembur += jam_lembur
    
    if total_lembur >= Maks_lembur_mingguan:
        print("Total jam lembur mingguan telah mencapai batas, lembur dihentikan.")
        break
    
    if jam_lembur == 0:
        tambahan_lembur = 0
    elif 1 <= jam_lembur < 4:
        tambahan_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        tambahan_lembur = 100000
    elif jam_lembur == 6:
        tambahan_lembur = 200000
    elif jam_lembur == 8:
        tambahan_lembur = 300000

    total_gaji += Gaji_harian + tambahan_lembur
    total_gaji_lembur += tambahan_lembur
    
total_gaji_mingguan = Gaji_harian * (hari if total_lembur < Maks_lembur_mingguan else hari - 1)


print(f"Total jam lembur selama satu minggu: {total_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_mingguan}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji}")
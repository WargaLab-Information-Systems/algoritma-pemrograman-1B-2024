gaji_harian = 100000
maks_lembur_per_hari = 8
maks_lembur_mingguan = 40

total_gaji_tanpa_lembur = 0
total_jam_lembur_mingguan = 0
total_gaji_lembur = 0

for hari in range(7):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari + 1}: "))
    
    # batas lembur maksimal per hari
    if jam_lembur > maks_lembur_per_hari:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = maks_lembur_per_hari
    
    # hitung total lembur mingguan
    if total_jam_lembur_mingguan + jam_lembur > maks_lembur_mingguan:
        jam_lembur = maks_lembur_mingguan - total_jam_lembur_mingguan
        total_jam_lembur_mingguan = maks_lembur_mingguan
        print(f"Lembur dihentikan, hanya {jam_lembur} jam lembur yang dihitung pada hari ke-{hari + 1}.")
        break
    else:
        total_jam_lembur_mingguan += jam_lembur

    #lembur per hari
    print(f"Lembur hari ke-{hari + 1}: {jam_lembur} jam")
    
    # hitung gaji harian tanpa lembur
    total_gaji_tanpa_lembur += gaji_harian
    
    # hitung gaji lembur
    if jam_lembur >= 8:
        total_gaji_lembur += 300000
    elif jam_lembur >= 6:
        total_gaji_lembur += 200000
    elif jam_lembur >= 4:
        total_gaji_lembur += 100000
    elif jam_lembur > 0:
        total_gaji_lembur += jam_lembur * 25000

print("\nTotal lembur selama satu minggu:", total_jam_lembur_mingguan, "jam")
print("Total gaji lembur selama satu minggu: Rp", total_gaji_lembur)
print("Total gaji mingguan tanpa lembur: Rp", total_gaji_tanpa_lembur)
print("Total gaji mingguan termasuk lembur: Rp", total_gaji_tanpa_lembur + total_gaji_lembur)


# variabel
gaji_harian = 100000  
empat_jam_lembur = 100000 
enam_jam_lembur = 200000  
delapan_jam_lembur = 300000  
tambahan_lembur_kurang_4_jam = 25000  # Bonus per jam untuk lembur 1-3 jam
batas_lembur_perhari = 8  
batas_lembur_mingguan = 40  
total_hari = 7  

# Variabel untuk perhitungan
total_gaji_reguler = 0
total_lembur_mingguan = 0
total_gaji_lembur = 0

# jam lembur setiap hari dan hitung total
print("Masukkan jumlah jam lembur untuk setiap hari:")

for hari in range(total_hari):
    jam_lembur = int(input(f"  Hari {hari + 1}: "))

    # jam lembur per hari
    if jam_lembur > batas_lembur_perhari:
        print("   Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0

    # jam lembur melebihi batas
    if total_lembur_mingguan + jam_lembur > batas_lembur_mingguan:
        print("  Total lembur mingguan mencapai batas, tidak ada tambahan lembur.")
        jam_lembur = 0

    # menghitung bonus lembur 
    bonus_lembur = 0
    if jam_lembur == 0:
        bonus_lembur = 0
    elif jam_lembur < 4:
        for _ in range(jam_lembur):  # Menghitung bonus lembur per jam
            bonus_lembur += tambahan_lembur_kurang_4_jam
    elif jam_lembur == 4:
        bonus_lembur = empat_jam_lembur
    elif jam_lembur == 6:
        bonus_lembur = enam_jam_lembur
    elif jam_lembur == 8:
        bonus_lembur = delapan_jam_lembur

    # menambahkan gaji lembur ke total
    total_gaji_lembur += bonus_lembur
    total_lembur_mingguan += jam_lembur

    # jam lembur yang disimpan 
    print(f"  Lembur Hari {hari + 1}: {jam_lembur} jam, Bonus: Rp{bonus_lembur}")

# Hitung total gaji reguler
total_gaji_reguler = gaji_harian * total_hari

# Hitung total gaji termasuk lembur
total_gaji_mingguan = total_gaji_reguler + total_gaji_lembur

# hasil akhir
print("Hasil Perhitungan Gaji Mas Ironi:")
print("------------------------------------")
print(f"Total lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_reguler}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")

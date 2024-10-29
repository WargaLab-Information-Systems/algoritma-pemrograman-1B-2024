gaji_harian = 100000
total_gaji_mingguan = 0
total_lembur_mingguan = 0
total_gaji_lembur = 0
hari = 0

for hari in range(7):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari + 1}: "))
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0 
    elif total_lembur_mingguan + jam_lembur >= 40:
        print("Total jam lembur dalam seminggu sudah mencapai batas, lembur dihentikan.")
        jam_lembur = 0 
    
    if jam_lembur == 0:
        tambahan_lembur = 0
    elif jam_lembur < 4:
        tambahan_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        tambahan_lembur = 100000
    elif jam_lembur == 6:
        tambahan_lembur = 200000
    elif jam_lembur == 8:
        tambahan_lembur = 300000

    total_gaji_lembur += tambahan_lembur
    total_lembur_mingguan += jam_lembur
    
    # Hitung total gaji harian
    total_gaji_mingguan += gaji_harian + tambahan_lembur

    # Tampilkan hasil per hari
    print(f"Total lembur hari ke-{hari + 1}: {jam_lembur} jam, Uang lembur: Rp{tambahan_lembur}")

# Tampilkan hasil akhir
print(f"\nTotal lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{gaji_harian * 7}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")
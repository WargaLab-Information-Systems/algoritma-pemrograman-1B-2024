# Inisialisasi variabel
gaji_harian = 100000
batas_lembur_per_hari = 8
batas_lembur_mingguan = 40

total_gaji_pokok = 0
total_gaji_lembur = 0
total_jam_lembur = 0

# Input jam lembur untuk setiap hari dan perhitungan lembur
for hari in range(1, 8):
    lembur = int(input(f"Jam lembur hari ke-{hari}: "))

    # Validasi batas lembur harian
    if lembur > batas_lembur_per_hari:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 0

    total_jam_lembur += lembur

    if total_jam_lembur > 40:
        print("Total lembur telah mencapai 40 jam, lembur dihentikan.")
        lembur -= (total_jam_lembur - 40)
        total_jam_lembur = 40

    # Hitung gaji lembur harian
    gaji_lembur = 0
    
    if lembur == 0:
        gaji_lembur
    elif lembur < 4:
        gaji_lembur += lembur * 25000
    elif lembur == 4 or lembur == 5 :
        gaji_lembur += 100000
    elif lembur == 6 or lembur == 7 :
        gaji_lembur += 200000
    elif lembur == 8:
        gaji_lembur += 300000

    total_gaji_lembur += gaji_lembur
    print(f"gaji lembur hari ke-{hari}: Rp{gaji_lembur:,}")
    

# Hitung total gaji mingguan tanpa lembur dan dengan lembur
total_gaji_pokok = gaji_harian * 7
total_gaji_mingguan = total_gaji_pokok + total_gaji_lembur

# Cetak hasil akhir
print("\n--- Rincian Gaji Mingguan ---")
print(f"Total lembur selama 7 hari: {total_jam_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur:,}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_pokok:,}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan:,}")
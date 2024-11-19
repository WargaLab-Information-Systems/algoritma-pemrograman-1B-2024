# Konstanta
gaji_harian = 100000
jam_lembur_maksimal = 8
jam_lembur_mingguan_maksimal = 40
bonus_lembur = {4: 100000, 6: 200000, 8: 300000}
tambahan_per_jam = 25000

# Variabel untuk menyimpan total gaji
total_gaji_mingguan = 0
total_lembur_mingguan = 0
total_gaji_lembur = 0

# Menghitung gaji selama 7 hari
for hari in range(1, 8):
    jam_lembur = int(input(f"Masukkan jam lembur untuk hari ke-{hari}: "))
    
    # Cek jam lembur
    if jam_lembur > jam_lembur_maksimal:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur_hari = 0
    else:
        lembur_hari = jam_lembur

    # Cek total jam lembur mingguan
    total_lembur_mingguan += lembur_hari
    if total_lembur_mingguan > jam_lembur_mingguan_maksimal:
        print("Total jam lembur dalam seminggu sudah mencapai batas maksimal. Lembur dihentikan.")
        break

    # Hitung gaji lembur
    if lembur_hari >= 4:
        total_gaji_lembur += bonus_lembur[lembur_hari]
    elif lembur_hari >= 1:
        total_gaji_lembur += lembur_hari * tambahan_per_jam

    # Tambahkan gaji harian
    total_gaji_mingguan += gaji_harian

# Hitung total gaji mingguan
total_gaji_mingguan += total_gaji_lembur

# Menampilkan hasil
print(f"Total lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_mingguan - total_gaji_lembur}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")
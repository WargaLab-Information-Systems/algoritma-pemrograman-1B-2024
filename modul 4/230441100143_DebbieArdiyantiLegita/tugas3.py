# Konfigurasi dasar
gaji_per_hari = 100000
maks_jam_lembur_harian = 8
maks_jam_lembur_mingguan = 40

jam_lembur_per_hari = [] # list untuk menyimpan data jumlah jam lembur harian selama satu minggu.

for hari in range(7):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari + 1}: "))
    
    if jam_lembur > maks_jam_lembur_harian:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0
    jam_lembur_per_hari.append(jam_lembur)

total_jam_lembur = 0
for jam in jam_lembur_per_hari:
    total_jam_lembur += jam

total_gaji_lembur = 0
if total_jam_lembur > maks_jam_lembur_mingguan:
    print("Lembur mingguan mencapai batas maksimal 40 jam, tidak dihitung lebih.")
    total_jam_lembur = maks_jam_lembur_mingguan  
else:
    for jam_lembur in jam_lembur_per_hari:
        if jam_lembur == 4:
            total_gaji_lembur += 100000
        elif jam_lembur == 6:
            total_gaji_lembur += 200000
        elif jam_lembur == 8:
            total_gaji_lembur += 300000
        elif 1 <= jam_lembur < 4:
            total_gaji_lembur += jam_lembur * 25000

gaji_mingguan_reguler = gaji_per_hari * 7

gaji_mingguan_total = gaji_mingguan_reguler + total_gaji_lembur

print("\n--- Hasil Perhitungan ---")
for hari in range(7):
    print(f"Lembur hari ke-{hari + 1}: {jam_lembur_per_hari[hari]} jam")
print(f"Total jam lembur selama satu minggu: {total_jam_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{gaji_mingguan_reguler}")
print(f"Total gaji mingguan termasuk lembur: Rp{gaji_mingguan_total}")

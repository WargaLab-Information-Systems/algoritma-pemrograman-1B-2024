gaji_harian = 100000
max_lembur_harian = 8
max_lembur_mingguan = 40

# inisialisasi variabel
total_lembur_mingguan = 0
total_bonus_lembur = 0

# perulangan untuk 7 hari
for hari in range(1, 8):
    print()
    print(f"Hari ke-{hari}")
    
    # input jam lembur dengan validasi
    while True:
        jam_lembur = int(input("Masukkan jam lembur: "))
        if jam_lembur < 0:
            print("Jam lembur tidak boleh negatif!")
            continue
        break
    
    # cek batas lembur harian
    if jam_lembur > max_lembur_harian:
        print("Lembur melebihi batas, tidak dihitung.")
        bonus_hari = 0
        jam_lembur = 0
    # cek batas lembur mingguan
    elif total_lembur_mingguan + jam_lembur > max_lembur_mingguan:
        print("Total lembur mingguan telah mencapai batas 40 jam.")
        bonus_hari = 0
        jam_lembur = 0
    else:
        # hitung bonus lembur berdasarkan jam
        if jam_lembur >= 1 and jam_lembur <= 3:
            bonus_hari = jam_lembur * 25000
        elif jam_lembur >= 4 and jam_lembur <= 5:
            bonus_hari = 100000
        elif jam_lembur >= 6 and jam_lembur <= 7:
            bonus_hari = 200000
        elif jam_lembur == 8:
            bonus_hari = 300000
        
        total_lembur_mingguan += jam_lembur
        total_bonus_lembur += bonus_hari
        
    print(f"Lembur hari ini: {jam_lembur} jam")
    print(f"Bonus lembur hari ini: Rp{bonus_hari:}")

# menghitung total gaji
total_gaji_tanpa_lembur = gaji_harian * 7
total_gaji_dengan_lembur = total_gaji_tanpa_lembur + total_bonus_lembur
print()

# menampilkan hasil akhir
print(f"Total jam lembur selama seminggu: {total_lembur_mingguan} jam")
print(f"Total bonus lembur: Rp{total_bonus_lembur:,}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_tanpa_lembur:,}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_dengan_lembur:,}")
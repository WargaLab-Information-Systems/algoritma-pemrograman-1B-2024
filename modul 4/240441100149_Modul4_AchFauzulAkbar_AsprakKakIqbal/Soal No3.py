# Inisialisasi variabel
gaji_harian = 100000
total_gaji_mingguan = 0
total_lembur_mingguan = 0
total_gaji_lembur = 0

# Input jam lembur per hari selama 7 hari
jam_lembur_per_hari = []

for i in range(7):
    jam_lembur = int(input(f"Masukkan jam lembur untuk hari ke-{i + 1}: "))
    jam_lembur_per_hari.append(jam_lembur)

# Proses perhitungan gaji
for i in range(7):
    jam_lembur = jam_lembur_per_hari[i]
    gaji_hari = gaji_harian
    lembur_hari = 0

    # Aturan lembur 
    if jam_lembur > 8:
        print(f"Hari {i + 1}: Lembur melebihi batas, tidak dihitung.")
        # jam_lembur = 8  # Batasi lembur sampai 8 jam

    if total_lembur_mingguan + jam_lembur >= 40:
        jam_lembur = max(0, 40 - total_lembur_mingguan)  # Hentikan lembur jika sudah mencapai 40 jam
        if jam_lembur == 0:
            print(f"Hari {i + 1}: Lembur telah dihentikan karena sudah mencapai batas 40 jam.")
        else:
            print(f"Hari {i + 1}: Lembur dibatasi menjadi {jam_lembur} jam.")

    # Hitung gaji lembur
    if jam_lembur == 0:
        lembur_hari = 0
    elif jam_lembur < 4:
        lembur_hari = jam_lembur * 25000
    elif jam_lembur == 4:
        lembur_hari = 100000
    elif jam_lembur == 6:
        lembur_hari = 200000
    elif jam_lembur == 8:
        lembur_hari = 300000

    total_gaji_lembur += lembur_hari
    total_lembur_mingguan += jam_lembur
    total_gaji_mingguan += gaji_hari + lembur_hari

    print(f"Hari {i + 1}: Lembur = {jam_lembur} jam, Gaji Lembur = Rp{lembur_hari}")

# Hitung total gaji mingguan tanpa lembur
total_gaji_mingguan += gaji_harian * 7  # Tambahkan gaji reguler untuk 7 hari

# Output hasil
print(f"\nTotal Lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total Gaji Lembur: Rp{total_gaji_lembur}")
print(f"Total Gaji Mingguan tanpa lembur: Rp{gaji_harian * 7}")
print(f"Total Gaji Mingguan termasuk lembur: Rp{total_gaji_mingguan + (gaji_harian * 7)}")
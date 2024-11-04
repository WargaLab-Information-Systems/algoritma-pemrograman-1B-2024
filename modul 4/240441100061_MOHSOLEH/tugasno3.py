# Konstanta
gaji_harian = 100000
maks_lembur = 8 
gaji_lembur = {  # Dictionary untuk gaji lembur berdasarkan jam lembur
    4: 100000,
    6: 200000,
    8: 300000
}
gaji_per_jam_kurang = 25000 #jika lembur di bawah 4 jam

total_gaji_mingguan = 0
total_gaji_lembur = 0
total_lembur = 0

# meminta input jam lembur sampai hari ke 7 
for hari in range(1, 8):
    lembur_hari = int(input(f"Masukkan jam lembur hari ke-{hari}: "))
# Memeriksa apakah jam lembur melebihi batas maksimum
    if lembur_hari > maks_lembur:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur_hari = 0 
    elif total_lembur + lembur_hari >= 40:
        print("Total jam lembur sudah mencapai batas maksimal, lembur dihentikan.")
        lembur_hari = 0 
    
    # Menambahkan jam lembur hari ini ke total jam lembur
    total_lembur += lembur_hari
    
    # Menghitung gaji lembur berdasarkan jam lembur
    if lembur_hari in gaji_lembur:
        total_gaji_lembur += gaji_lembur[lembur_hari]
    elif 1 <= lembur_hari < 4:
        total_gaji_lembur += lembur_hari * gaji_per_jam_kurang

    # Menambahkan gaji harian ke total gaji mingguan.
    total_gaji_mingguan += gaji_harian

    
# Menambahkan total gaji lembur ke total gaji mingguan.
total_gaji_mingguan += total_gaji_lembur

print("\nRingkasan Gaji Mas Ironi:")
print(f"Total lembur selama satu minggu : {total_lembur} jam")
print(f"Total gaji lembur : Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur : Rp{gaji_harian * 7}")
print(f"Total gaji mingguan termasuk lembur : Rp{total_gaji_mingguan}")
# Mencetak ringkasan gaji, termasuk total jam lembur, 
# total gaji lembur, total gaji mingguan tanpa lembur, dan total gaji mingguan termasuk lembur.
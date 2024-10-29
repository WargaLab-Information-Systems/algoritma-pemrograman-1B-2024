gaji_harian = 100000
lembur_per_hari = []  
total_lembur_seminggu = 0 
total_gaji_lembur = 0 

for hari in range(1, 8):  
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari}: "))
    
    if jam_lembur > 8:
        print("PERINGATAN !!! Lembur melebihi batas, tidak akan dihitung, ISTIRAHATLAH.")
        jam_lembur = 8  
    lembur_per_hari.append(jam_lembur)
    
    total_lembur_seminggu += jam_lembur

    if total_lembur_seminggu >= 40:
        print("Total lembur telah mencapai 40 jam, lembur dihentikan.")
        lembur_per_hari[-1] = 40 - (total_lembur_seminggu - jam_lembur)
        total_lembur_seminggu = 40
        break

for jam_lembur in lembur_per_hari:
    if jam_lembur == 0:
        gaji_lembur_harian = 0 
    elif 1 <= jam_lembur < 4:
        gaji_lembur_harian = 25000 * jam_lembur  
    elif jam_lembur == 4:
        gaji_lembur_harian = 100000  
    elif jam_lembur == 6:
        gaji_lembur_harian = 200000  
    elif jam_lembur == 8:
        gaji_lembur_harian = 300000  

    total_gaji_lembur += gaji_lembur_harian  

gaji_mingguan_tanpa_lembur = gaji_harian * 7
total_gaji_mingguan = gaji_mingguan_tanpa_lembur + total_gaji_lembur

print("\nRingkasan:")

for hari, jam_lembur in enumerate(lembur_per_hari, 1):
    print(f"Lembur hari ke-{hari}: {jam_lembur} jam")

print(f"Total lembur selama seminggu: {total_lembur_seminggu} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{gaji_mingguan_tanpa_lembur}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")
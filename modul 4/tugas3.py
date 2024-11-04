
gajiperhari = 100000
lembur_max_perhari = 8
lembur_max_perminggu = 40 
tot_gaji_reg_perminggu = 7 * gajiperhari
tot_lembur_perminggu = 0
tot_gaji_lembur_perminggu = 0


for i in range (1,8):
    jam_lembur = int(input(f"Masukkan berapa jam lembur hari ke {i}: "))
    if jam_lembur > lembur_max_perhari:
        print("Lembur melebihi batas jam lembur harian, maka tidak dihitung")
        jam_lembur = 0
    tot_lembur_perminggu += jam_lembur
    if tot_lembur_perminggu >= lembur_max_perminggu:
        print("Lembur dalam seminggu mencapai atau melebihi 40 jam, lembur akan dihentikan")
        break
    
    gaji_lembur_perhari = 0
    if jam_lembur < 4:
        gaji_lembur_perhari += jam_lembur*25000
    if jam_lembur == 4:
        gaji_lembur_perhari += 100000
    if jam_lembur == 6:
        gaji_lembur_perhari += 200000
    if jam_lembur == 8:
        gaji_lembur_perhari += 300000

    tot_gaji_lembur_perminggu += gaji_lembur_perhari
    print(f"Lembur hari ke {i} menghabiskan {jam_lembur} jam lembur")

    print("===GAJI MAS IRONI===")
    print(f"Total lembur selama satu minggu adalah {tot_lembur_perminggu}")
    print(f"Total gaji lembur adalah Rp. {tot_gaji_lembur_perminggu}")
    print(f"Total gaji reguler adalah Rp. {tot_gaji_reg_perminggu}")
    print(f"Total gaji yang di dapat adalah Rp. {tot_gaji_reg_perminggu + tot_gaji_lembur_perminggu}")
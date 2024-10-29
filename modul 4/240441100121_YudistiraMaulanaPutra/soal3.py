gajiHarian, maxLemburHari, maxLemburMinggu = 100000, 8, 40
totalGajiMingguan = 0
totalLemburMingguan = 0
totalGajiLembur = 0
bonusLembur = 0
for hari in range(1,8):
    jamLembur = int(input(f"Jam lembur ke-{hari}: "))
    if jamLembur > 8:  
        print("Lembur maximal, tidak akan dihitung.")
    else:
        if jamLembur <= 3:
            bonusLembur = jamLembur * 25000
        if jamLembur == 4:
            bonusLembur = 100000
        if jamLembur == 6:
            bonusLembur = 200000
        if jamLembur == 8:
            bonusLembur = 300000

    totalLemburMingguan += jamLembur
    totalGajiLembur += bonusLembur
    totalGajiMingguan += gajiHarian 

print(f"\nTotal lembur 7 hari: {totalLemburMingguan} jam")
print(f"Total gaji lembur: Rp{totalGajiLembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{totalGajiMingguan}")
print(f"Total gaji mingguan plus lembur: Rp{totalGajiMingguan + totalGajiLembur + bonusLembur}")
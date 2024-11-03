Gaji_Harian = 100000
Total_Gaji_Lembur = 0
Total_Lembur = 0

for i in range(7):
    Lembur = int(input(f"Masukkan jam lembur hari ke-{i + 1} : "))
    
    if Lembur > 8:
        print("Lembur melebihi batas, tidak dihitung")
    elif Total_Lembur + Lembur > 40:
        print("Total lembur melebihi 40 jam, lembur dihentikan")
        break
    elif Lembur <= 3:
        Gaji_Lembur = 25000 * Lembur
    elif Lembur == 4:
        Gaji_Lembur = 100000
    elif Lembur == 6:
        Gaji_Lembur = 200000
    elif Lembur == 8:
        Gaji_Lembur = 300000
    else:
        Gaji_Lembur = Lembur * 25000

    Total_Lembur += Lembur
    Total_Gaji_Lembur += Gaji_Lembur

Total_Gaji_Harian = Gaji_Harian * 7
Total_Gaji_Harian_dan_Lembur = Total_Gaji_Harian + Total_Gaji_Lembur

print(f"Total lembur dalam 7 hari adalah {Total_Lembur} jam")
print(f"Total Gaji lembur adalah Rp.{Total_Gaji_Lembur}")
print(f"Total Gaji Harian adalah Rp.{Total_Gaji_Harian}")
print(f"Total Gaji Harian + Gaji Lembur adalah Rp.{Total_Gaji_Harian_dan_Lembur}")




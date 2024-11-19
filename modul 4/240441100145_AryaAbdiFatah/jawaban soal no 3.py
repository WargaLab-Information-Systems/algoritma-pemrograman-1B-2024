gajiHarian = 100000 
totalGajiPokok = gajiHarian * 7
lemburPerjam = 25000
lembur4jam = 100000
lembur6jam = 200000
lembur8jam = 300000
 
jamLembur = 0
GajiLembur = 0
totalJamLembur = 0
totalGajiLembur = 0


for hari in range (1, 8): 
    if totalJamLembur >= 40: #gaji lembur untuk seminggu
        print(f"Total jam lembur {totalJamLembur} jam, melebihi batas, lembur dihentikan")
        break
    
    jamLembur = int(input(f"Masukkan jam lembur pada hari ke-{hari}: ")) #masukan jam lembur
    if jamLembur > 8: # Max perhari 8 jam
        print(f"Hari ke-{hari} lembur melebihi batas, tidak dihitung")
        GajiLembur = 0
        
    if jamLembur == 0:
        GajiLembur = 0
        
    if jamLembur >= 1 and jamLembur <= 3:
        GajiLembur = lemburPerjam * jamLembur
        
    elif jamLembur >= 4 and jamLembur <=5:   
        GajiLembur = lembur4jam
            
    elif jamLembur >= 6 and jamLembur <=7:
        GajiLembur = lembur6jam
                
    elif jamLembur == 8:
        GajiLembur = lembur8jam
        
    print(f"Hari ke-{hari}, jam lembur = {jamLembur} jam dan gaji lembur = Rp.{GajiLembur}")
    totalGajiLembur += GajiLembur
    totalJamLembur += jamLembur
    
print("========RangkumanGaji======")
print(f"Total jam lembur selama seminggu = {totalJamLembur} jam")
print(f"Total gaji lembur selama seminggu = {totalGajiLembur}")
print(f"Total gaji seminggu tanpa lembur = {totalGajiPokok}")
print(f"Total gaji seminggu termasuk lembur = {totalGajiPokok+totalGajiLembur}")
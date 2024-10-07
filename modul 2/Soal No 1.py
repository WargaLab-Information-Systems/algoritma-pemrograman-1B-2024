n = input('masukan nama anda!')
m = int(input('masukan NIM anda!'))
nilai_UAS = int(input('masukan nilai UTS anda!'))
nilai_UTS = int(input('masukan nilai UAS anda!'))
nilai_akhir = (nilai_UAS + nilai_UTS) / 2
if nilai_akhir > 90:
    print("Nilai anda A")
elif nilai_akhir > 80:
    print('nilai anda B')
elif nilai_akhir > 70: 
    print('nilai anda C')
elif nilai_akhir > 60:
    print('nilai anda D')
elif nilai_akhir > 40:
    print('nilai anda E')
else:
    print('coba lagi')
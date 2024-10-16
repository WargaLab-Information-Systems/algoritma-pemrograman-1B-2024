n = input('masukan nama anda!')
m = int(input('masukan NIM anda!'))
nilai_UAS = int(input('masukan nilai UTS anda!'))
nilai_UTS = int(input('masukan nilai UAS anda!'))
nilai_akhir = (nilai_UAS + nilai_UTS) / 2
# print(f"nilai akhir adalah {nilai_akhir}")
if 80 < nilai_akhir <= 100:
    print('nilai anda A')
elif 70 < nilai_akhir <= 80:
    print('nilai anda B')
elif 60 < nilai_akhir <= 70: 
    print('nilai anda C')
elif 40 < nilai_akhir <= 60:
    print('nilai anda D')
elif 0 < nilai_akhir <= 40:
    print('nilai anda E')
else:
    print('coba lagi')
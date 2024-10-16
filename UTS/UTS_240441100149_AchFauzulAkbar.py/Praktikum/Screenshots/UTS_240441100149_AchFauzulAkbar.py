waktu = 0

while waktu>0:
    makan = input('apakah kamu sudah makan? ')
    if makan =='iya':
        continue
    elif makan =='belum':
        waktu+=15
        print('kamu memiliki waktu makan selama', waktu)
        
    mandi = input('apakah kamu sudah mandi ? ')
    if mandi =='sudah':
        continue
    elif mandi =='belum':
        waktu+=10
    print('kamu memiliki waktu selama', waktu)
else:
    
    transportasi = input('transportasi apa yang kamu gunakan [jalan kaki/motor]?')
if transportasi =='motor':
    waktu+=15
    print('kamu memiliki waktu ke kampus selama', waktu)
elif transportasi =='jalan kaki':
    waktu+=30
    print('kamu memiliki waktu ke kampus selama', waktu)
else:
    print('gas')
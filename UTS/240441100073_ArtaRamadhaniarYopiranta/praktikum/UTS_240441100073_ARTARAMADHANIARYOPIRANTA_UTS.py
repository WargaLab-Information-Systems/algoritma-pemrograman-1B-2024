makan = input("apakah anda sudah makan? (ya/tidak) ")
mandi = input("apakah anda sudah mandi? (ya/tidak )")
transportasi = input("pilih transporatasi untuk ke kampus? (jalan kaki/ motor)")

waktumakan = 15
waktumandi = 10
motor = 15
jalankaki = 30
totalpersiapan = waktumakan + waktumandi 
totalberangkatm = totalpersiapan + motor
totalberangkatj = totalpersiapan + jalankaki

if makan == 'tidak':
    print("silahkan makan, waktu anda 15 menit ")
if mandi == 'tidak':
    print("silahkan mandi, waktu anda 10 menit")
if transportasi == 'motor':
    print("total waktu yang anda habiskan adalah [totalberangkatm] menit, kamu berangkat tepat waktu")
else: 
    print("total waktu yang anda habiskan adalah [totalberangkatj] menit, kamu telat ke kampus")
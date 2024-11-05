#SEMANGAT NGAMPUS

total_waktu = int()
sampai =""

makan = input("kamu sudah makan? (ya/tidak)").lower()
if makan == "ya":
    print("kamu menghemat 15 menit") 
else: 
    total_waktu += 15
    print("kamu perlu makan terlebih dahulu")
    
mandi = input("kamu sudah mandi? (ya/tidak)").lower()
if mandi == "ya":
    print("kamu menghemat waktu 10 menit")
else:
    total_waktu += 10
    print("kamu perlu mandi terlebih dahulu")
    
tranportasi = input("Sekarang, kamu harus menentukan tranportasi apa yang akan kamu gunakan untuk bisa sampai ke sekolah (jalan/motor) : ").lower()
if tranportasi == "jalan":
    total_waktu += 30 
    print("Kamu berjalan untuk ke kampus, jadi waktu yang kamu tempuh untuk sampai yaitu 30 menit")
elif tranportasi == "motor":
    total_waktu += 15
    print("kamu memilih untuk menggunakan motor ke kampus, jadi waktu yang akan kamu tempuh yaitu 15 menit")
    
if total_waktu > 50:
    sampai += "terlambat"
else:
    sampai += "tidak terlambat"

print()
print("..................total alokasi waktu yang dibutuhkan..................")
print(f"dari persiapan pagi ini yang telah kamu lakukan, kamu memerlukan waktu sebanyak {total_waktu} menit untuk sampai ke kampus")
print("dan dari total waktu yang digunakan untuk ke kampus, maka kamu", sampai )

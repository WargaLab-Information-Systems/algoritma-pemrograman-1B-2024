makan = input("Apakah kamu sudah makan? (ya/tidak)")
mandi = input("Apakah kamu sudah mandi? (ya/tidak)")
cek_transportasi = input("Pilih transportasi kendaraan! (jalankaki/motor)")
total_waktu = 0
waktu_maksimal = 50

if makan == 'ya':
    if makan == 'tidak':
        if makan == 'tidak':
            total_waktu += 15
            
if mandi == 'ya':
    if mandi == 'tidak':
        if mandi == 'tidak':
            total_waktu += 10
            
if cek_transportasi == 'jalankaki':
    if cek_transportasi == 'jalankaki':
        total_waktu += 30
        
if cek_transportasi == 'motor':
    if cek_transportasi == 'motor':
        total_waktu += 15
        
if total_waktu < waktu_maksimal:
    print("Anda berangkat tepat waktu")
else:
    print("Anda terlambat")
print(f"Total waktu persiapan dan perjalanan: {total_waktu} menit")

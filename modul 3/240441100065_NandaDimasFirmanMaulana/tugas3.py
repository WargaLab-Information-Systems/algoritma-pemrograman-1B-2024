# 3
ulang = 'y' 
while ulang == 'y' : 
   pinjam = int(input("Masukkan lama waktu penyewaan DVD (dalam hari) : ")) 
   batas = 5
   denda_h = 2500
   tambahan = 5500 #jika terlambat lebih dari 10 hari 
   total_denda = 0 

   if pinjam > batas :
      terlambat = pinjam - batas
      total_denda = terlambat * denda_h 
      if terlambat > 10: 
       tambah_hari = terlambat - 5 
       denda_tambahan = (tambah_hari // 5) * tambahan 
       total_denda += denda_tambahan

   print(f"Total denda keterlambatan adalah Rp {total_denda}")

else: print("DVD dikembalikan tepat waktu, tidak ada denda.")
ulang = input("Apakah ingin menghitung kembali? (y/t): ") 
print("Terima kasih!")

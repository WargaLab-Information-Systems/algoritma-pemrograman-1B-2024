

# Inisialisasi variabel waktu persiapan
waktu_persiapan = 0

# Cek status makan
while True:
    status_makan = input("Apakah Anda sudah makan? (ya/tidak): ")
    if status_makan in ['ya', 'tidak']:
        break
    print("Mohon masukkan 'ya' atau 'tidak'.")

if status_makan == 'tidak':
    waktu_persiapan += 30  

# Cek status mandi
while True:
    status_mandi = input("Apakah Anda sudah mandi? (ya/tidak): ")
    if status_mandi in ['ya', 'tidak']:
        break
    print("Mohon masukkan 'ya' atau 'tidak'.")

if status_mandi == 'tidak':
    waktu_persiapan += 20  

# Cek status transportasi
while True:
    status_transportasi = input("Apakah transportasi tersedia? (ya/tidak): ")
    if status_transportasi in ['ya', 'tidak']:
        break
    print("Mohon masukkan 'ya' atau 'tidak'.")

if status_transportasi == 'tidak':
    waktu_persiapan += 15  

# Input waktu tersisa
waktu_tersisa = int(input("Berapa menit waktu yang tersisa sebelum Anda harus berangkat? "))

# Evaluasi kesiapan
if waktu_persiapan <= waktu_tersisa:
    print(f"Anda memiliki cukup waktu! Waktu persiapan yang dibutuhkan: {waktu_persiapan} menit.")
    print("Anda bisa berangkat tepat waktu.")
else:
    print(f"Perhatian! Waktu persiapan yang dibutuhkan ({waktu_persiapan} menit) lebih lama dari waktu yang tersisa ({waktu_tersisa} menit).")
    print("Anda mungkin akan terlambat. Pertimbangkan untuk mempercepat persiapan atau mengatur ulang jadwal Anda.")
 
 
 
    
    
    

    
    
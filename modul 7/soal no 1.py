alat_kesehatan = {
    'alat_pengukur_tekanan_darah ': 2,  
    'termometer': 3,          
    'stetoskop': 4            
}

# Pengembalian alat setelah seminggu
alat_kesehatan['alat_pengukur_tekanan_darah '] -= 1
alat_kesehatan['termometer'] -= 2          

# Penukaran alat (menukar 3 stetoskop dengan 2 inhaler)
alat_kesehatan['stetoskop'] -= 3            # Mengurangi 3 stetoskop
alat_kesehatan['inhaler'] = 2               # Menambah 2 inhaler

# Menampilkan hasil alat yang dipinjam saat ini
print("Alat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in alat_kesehatan.items():   # # items untuk mengembalikan sebuah objek yg dapat diiterasi yang berisi pasangan kunci dan nilai
    print(f"{alat.capitalize()}: {jumlah}")
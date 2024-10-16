# Variabel 
BATAS_PINJAM = 5
DENDA_PER_HARI = 2500
DENDA_TAMBAHAN = 5500
LONCATAN_DENDA_TAMBAHAN = 5

lanjut = 'yes'

# Loop
while lanjut == 'yes':
    lama_pinjam = int(input("lama peminjaman DVD : "))
    
    if lama_pinjam < 0:
        print("Lama peminjaman tidak boleh negatif.")
    else:
        # Hitung denda
        if lama_pinjam <= BATAS_PINJAM:
            total_denda = 0
        else:
            keterlambatan = lama_pinjam - BATAS_PINJAM
            
            # Hitung denda normal
            denda_normal = keterlambatan * DENDA_PER_HARI

             # Menghitung denda tambahan
            denda_tambahan_total = 0
            
            if keterlambatan >= 10:
                denda_tambahan_total = ((keterlambatan - 10) // LONCATAN_DENDA_TAMBAHAN + 1) * DENDA_TAMBAHAN
            
            total_denda = denda_normal + denda_tambahan_total

        print(f"Total denda: Rp {total_denda:,}")
    
    # untuk mengulang program
    lanjut = input("Apakah Anda ingin menghitung lagi? (yes/no): ")

print("Terima kasih telah berkunjung ke toko penyewaan DVD terbaik se kwangya!")
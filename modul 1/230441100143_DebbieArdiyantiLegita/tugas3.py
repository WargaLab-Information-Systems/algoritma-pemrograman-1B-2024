def hitung_nilai_tukar(USD, usd_kurs=25000):
    return USD * usd_kurs

USD = 35  
usd_kurs = 25000  

Hasil_tukar = hitung_nilai_tukar(USD, usd_kurs)

print(f"Jumlah Rupiah yang akan didapatkan Suraji: Rp {Hasil_tukar:,.2f}")
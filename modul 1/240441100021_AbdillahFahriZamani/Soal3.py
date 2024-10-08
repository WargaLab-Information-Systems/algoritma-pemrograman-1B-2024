# Diket nilai kurs pada tanggal praktikum Rp.15.184, dan suraji mempunyai uang $35
# Input nilai kurs pada tanggal praktikum
nilai_kurs = float(input("Masukkan nilai kurs pada tanggal praktikum: "))

# Input uang dolar
uang_dolar = float(input("Masukkan jumlah uang dolar: "))

# Mengkonversi dolar ke rupiah
uang_rupiah = uang_dolar * nilai_kurs

# Hasil
print(f"Uang yang didapat Suraji setelah menukarkan US${uang_dolar} ke Rupiah adalah Rp{uang_rupiah:.2f}")

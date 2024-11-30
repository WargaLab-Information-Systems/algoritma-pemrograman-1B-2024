# #4 Menghitun berapa banyak cara untuk mandor membentuk tim
jumlah = 7
dipilih = 4
if dipilih > jumlah :
    print("Jumlah yang ingin dipilih tidak boleh lebih dari total anggota tim.")
else:
# Menghitung faktorial dari jumlah, dipilih,dan(jumlah - dipilih) secara langsung
    faktorial_jumlah = 1
    for i in range(1, jumlah + 1):
        faktorial_jumlah *= i
    faktorial_dipilih = 1
    for i in range(1, dipilih + 1):
        faktorial_dipilih *= i

    faktorial_sisa = 1
    for i in range(1, (jumlah - dipilih) + 1):
     faktorial_sisa *= i

# Menghitung kombinasi
kombinasi = faktorial_jumlah // (faktorial_dipilih*faktorial_sisa)
    
    # Output hasil
print(f"Jumlah cara untuk memilih {dipilih} orang dari {jumlah} orang adalah: {kombinasi}")
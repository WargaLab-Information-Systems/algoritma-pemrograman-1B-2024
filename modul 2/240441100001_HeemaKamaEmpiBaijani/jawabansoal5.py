nama = input("Masukan Nama Pembeli : ")
usia = int(input("Masukan Usia Pembeli : "))
if usia < 18:
    print("Maaf usia anda belum mencukupi")
else:
    totalBelanja = float(input("Masukan Total Belanja : "))
    punyaKartuMember = True if input("Apakah Pembeli Memiliki Kartu Member? (Ya/Tidak) : ") == "ya" else False
    diskon = 1 - 0.15 if punyaKartuMember else 1

    if totalBelanja >= 500000:
        diskon -= 0.1
    
    totalHargaSetelahDiskon = totalBelanja * diskon
    print(f"Nama Pembeli : {nama}")
    print(f"Diskon yang didapatkan : {(1 - diskon) * 100:.2f}%")
    print(f"Total Harga Sebelum Diskon : {totalBelanja}")
    print(f"Total Harga Setelah Diskon : {totalHargaSetelahDiskon}")
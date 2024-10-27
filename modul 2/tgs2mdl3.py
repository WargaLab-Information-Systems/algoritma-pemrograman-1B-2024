# Program untuk membalikkan urutan angka
while True:
    try:
        angka = int(input("Masukkan angka bulat: "))  # Meminta input angka
        angka_balik = 0

        while angka > 0:
            sisa = angka % 10  # Mendapatkan digit terakhir
            angka_balik = (angka_balik * 10) + sisa  # Menambahkan digit ke angka_balik
            angka //= 10  # Mengurangi angka dengan membuang digit terakhir

        print("Angka setelah dibalik:", angka_balik)
        
        # Meminta konfirmasi untuk melanjutkan
        ulang = input("Ingin membalikkan angka lagi? (y/n): ").lower()
        if ulang != 'y':
            break  # Keluar dari loop jika tidak ingin melanjutkan
    except ValueError:
        print("Input tidak valid, masukkan angka bulat.")
        continue  # Melanjutkan ke input berikutnya jika input tidak valid
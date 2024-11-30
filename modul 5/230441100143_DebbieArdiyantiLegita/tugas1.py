def calculate_discount():
    # Input total belanja secara dinamis
    try:
        total_belanja = float(input("Masukkan total belanja: Rp. "))
    except ValueError:
        print("Input harus berupa angka!")
        return
    
    # Input jenis membership
    print("\nPilih jenis membership:")
    print("1. Gold")
    print("2. Silver")
    print("3. Bronze")
    print("4. Non-member")
    membership = input("Masukkan pilihan (1-4): ")
    
    # Inisialisasi diskon
    diskon = 0
    
    # Menentukan diskon berdasarkan membership
    if membership == "1":
        diskon = 15
        jenis = "Gold"
    elif membership == "2":
        diskon = 10
        jenis = "Silver"
    elif membership == "3":
        diskon = 5
        jenis = "Bronze"
    elif membership == "4":
        diskon = 0
        jenis = "Non-member"
    else:
        print("Pilihan membership tidak valid!")
        return
    
    # Cek tambahan diskon untuk belanja > 1 juta
    if total_belanja > 1000000:
        diskon += 5
    
    # Hitung jumlah diskon dan total bayar
    jumlah_diskon = total_belanja * (diskon/100)
    total_bayar = total_belanja - jumlah_diskon
    
    # Tampilkan hasil
    print("\n===== Detail Pembayaran =====")
    print(f"Total Belanja: Rp. {total_belanja:,.2f}")
    print(f"Jenis Membership: {jenis}")
    print(f"Besar Diskon: {diskon}%")
    print(f"Jumlah Diskon: Rp. {jumlah_diskon:,.2f}")
    print(f"Total Bayar: Rp. {total_bayar:,.2f}")
    print("===========================")
    
    return total_bayar, jumlah_diskon, diskon

while True:
    # Panggil fungsi calculate_discount
    hasil = calculate_discount()
    
    if hasil:
        total_bayar, jumlah_diskon, diskon = hasil
    
    # Tanya apakah ingin menghitung lagi
    lanjut = input("\nHitung diskon lagi? (y/n): ")
    if lanjut.lower() != 'y':
        print("Terima kasih telah menggunakan program ini!")
        break
def program_diskon():
    nama = input("Masukkan nama pembeli: ")
    usia = int(input("Masukkan usia pembeli: "))
    
    if usia < 18:
        print("Maaf, usia anda belum mencukupi.")
        return
    
    total_belanja = float(input("Masukkan total belanja: Rp "))
    member = input("Punya kartu member? (punya/tidak): ")

    diskon = (15 if member == 'punya' else 0) + (10 if total_belanja > 500000 else 0)
    
    total_setelah_diskon = total_belanja - (total_belanja * diskon / 100)
    
    # Tampilkan hasil
    print("Nama: " + nama)
    print("Diskon:", diskon, "%")
    print("Total sebelum diskon:", total_belanja)
    print("Total setelah diskon:", total_setelah_diskon)

program_diskon()

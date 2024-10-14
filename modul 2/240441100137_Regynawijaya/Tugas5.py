# Program Diskon Pembelian Minuman

# Input data pembeli
nama = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))

# Jika usia di bawah 18, program berhenti
if usia < 18:
    print("Maaf usia anda belum mencukupi.")
else:
    # Lanjutkan jika usia mencukupi
    member = input("Apakah Anda memiliki kartu member (y/n): ").lower()
    total_belanja = float(input("Masukkan total belanja: Rp"))

    # Inisialisasi diskon
    diskon = 0

    # Diskon member 15%
    if member == 'y':
        diskon += 0.15

    # Diskon tambahan jika total belanja lebih dari Rp500.000
    if total_belanja > 500000:
        diskon += 0.10

    # Hitung total diskon
    total_diskon = total_belanja * diskon
    harga_setelah_diskon = total_belanja - total_diskon

    # Tampilkan hasil
    print("\n--- Rincian Pembelian ---")
    print(f"Nama Pembeli: {nama}")
    print(f"Total Harga Sebelum Diskon: Rp{total_belanja:.2f}")
    print(f"Diskon yang Didapatkan: Rp{total_diskon:.2f}")
    print(f"Total Harga Setelah Diskon: Rp{harga_setelah_diskon:.2f}")


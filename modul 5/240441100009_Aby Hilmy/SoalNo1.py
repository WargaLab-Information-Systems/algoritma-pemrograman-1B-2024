def hitungan_diskon(total_belanja, keanggotaan):
    # Inisialisasi diskon
    diskon = 0

    # menentukan diskon berdasarkan jenis keanggotaan
    if keanggotaan == "Gold":
        diskon = 0.15
    elif keanggotaan == "Silver":
        diskon = 0.10
    elif keanggotaan == "Bronze":
        diskon = 0.05
    elif keanggotaan == "None":
        diskon = 0.0
    
    # Cek apakah total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 0.05  # Tambahan diskon 5%

    # Hitung total diskon
    total_diskon = total_belanja * diskon
    return total_diskon

# Menampilkan hasil dan menanyakan input pengguna
total_belanja = int(input("masukkan total belanja:"))
keanggotaan = str(input("masukkan keanggotanmu:"))
diskon = hitungan_diskon(total_belanja, keanggotaan)
print(f"Diskon yang didapat: {diskon}",keanggotaan)

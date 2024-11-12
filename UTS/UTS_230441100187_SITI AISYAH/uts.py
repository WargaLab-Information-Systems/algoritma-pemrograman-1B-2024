# Program "Semangat Ngampus!"

# Fungsi untuk menghitung waktu persiapan dan perjalanan
def hitung_waktu_persiapan_dan_perjalanan(sudah_makan, sudah_mandi, transportasi):
    # Waktu persiapan
    waktu_makan = 15 if sudah_makan == "tidak" else 0
    waktu_mandi = 10 if sudah_mandi == "tidak" else 0

    # Waktu perjalanan berdasarkan transportasi
    if transportasi == "jalan kaki":
        waktu_perjalanan = 30
    elif transportasi == "motor":
        waktu_perjalanan = 15
    else:
        return "Transportasi tidak valid."

    # Total waktu persiapan dan perjalanan
    total_waktu = waktu_makan + waktu_mandi + waktu_perjalanan

    # Menentukan apakah terlambat atau tidak
    if total_waktu <= 50:
        return f"Total waktu persiapan dan perjalanan: {total_waktu} menit\nKamu berangkat tepat waktu."
    else:
        return f"Total waktu persiapan dan perjalanan: {total_waktu} menit\nKamu terlambat."

# Input dari pengguna
sudah_makan = input("Sudah makan? (ya/tidak): ").lower()
sudah_mandi = input("Sudah mandi? (ya/tidak): ").lower()
transportasi = input("Pilih transportasi (jalan kaki/motor): ").lower()

# Memanggil fungsi dan menampilkan hasil
hasil = hitung_waktu_persiapan_dan_perjalanan(sudah_makan, sudah_mandi, transportasi)
print(hasil)
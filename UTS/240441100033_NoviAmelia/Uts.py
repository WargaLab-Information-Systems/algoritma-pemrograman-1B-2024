# Input untuk status aktivitas
makan = input("Apakah kamu sudah makan? (ya/tidak): ").lower() == "ya"
minum = input("Apakah kamu sudah minum (Ya/tidak)")
mandi = input("Apakah kamu sudah mandi? (ya/tidak): ").lower() == "ya"
transportasi = input("mekamai transportasi apa untuk ke kampus? (jalan kaki/motor): ").lower()
jalanKaki = "30 menit"
motor = "15 menit"
if transportasi != jalanKaki:
    print(f"untuk menuju ke kampus membutuhkan waktu selama{jalanKaki}")
waktu_tersisa = int(input("Berapa menit waktu tersisa sebelum harus berangkat? "))

#mengecek apakah siap atau tidak
if makan and mandi and transportasi and waktu_tersisa >= 10:
    print("Kamu siap berangkat ke kampus!")
elif waktu_tersisa < 10:
    print("Waktu tidak cukup untuk berangkat tepat waktu!")
else:
    print("Kamu belum siap berangkat ke kampus.")
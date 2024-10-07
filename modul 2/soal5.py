nama_pembeli = input("MASUKKAN NAMA NAMA ANDA: ")
usia = int(input("BERAPA USIA ANDA: "))
member = (input("APAKAH KAMU PUNYA MEMBER: ya/tidak ="))
total_belanja = int(input("MASUKKAN TOTAL BELANJA ANDA: "))
diskon_member = 0.15

if usia < 18:
    print("MAAF USIA ANDA BELUM CUKUP")
if member == "ya":
    print("SELAMAT ANDA MENDAPATKAN DISKON SEBESAR 15% CUKUP MEMBAYAR", total_belanja - (diskon_member * total_belanja))
    print("Nama pembeli", nama_pembeli)
    print("Total Sebelum diskon", total_belanja)
else:
    print("Anda harus membayar sebesar", total_belanja)
    print("Nama pembeli", nama_pembeli)

belanja_500k = 0.10

if usia < 18:
    print("MAAF USIA ANDA TIDAK CUKUP")
elif total_belanja > 500000:
    print("SELAMAT ANDA MENDAPATKAN DISKON SEBESAR 10% DAN CUKUP MEMBAYAR", total_belanja - (belanja_500k * total_belanja))
    print("NAMA PEMBELI:", nama_pembeli)
    print("TOTAL BELANJA SEBELUM DISKON", total_belanja)
else:
    print("TOTAL YANG HARUS DIBAYAR SEBESAR", total_belanja)
    print("NAMA PEMBELI:", nama_pembeli)
# waktu_sampain_kampus = int("60")
# makan =input("apakah kamu sudah makan (ya/tidak): ")
# if makan == "ya":
#     makan_int+=int(15)
#     print("waktu yang di hemat 15 mnt")
# else:
#     print("waktu yang kamu perlukan 15 mnt")

# mandi =input("apakah kamu sudah mandi (ya/tidak): ")
# if mandi == "ya":
#     mandi+=10
#     print("waktuu yang di hemat 10 mnt")
# else:
#     print("waktu yang kamu perlukan 10 mnt")
# kendaraan =input("kamun akn menggunakan kendaraan apa = (sepeda/motor): ")
# if kendaraan == "sepeda":
#     kendaraan+=30
#     print("waktuu yang digunnakan 30 mnt]")
# else:
#     kendaraan+=15
#     print("waktu yang kamu perlukan 15 mnt")
# total_waktu = makan + mandi + kendaraan 
# print("waktu yang anda gunakan adalah",total_waktu,"menit")
# if total_waktu>waktu_sampain_kampus:
#     print("anda terlambat")
# elif total_waktu<waktu_sampain_kampus:
#     print("anda tepat waktu")
# else:
#     print("selesai")

# waktu_sampain_kampus = 60
# makan = input("apakah kamu sudah makan (ya/tidak): ")
# if makan == "ya":
#     waktu_hemat_makan = 15
#     print("waktu yang dihemat 15 menit")
# else:
#     waktu_hemat_makan = 0
#     print("waktu yang kamu perlukan 15 menit")

# mandi = input("apakah kamu sudah mandi (ya/tidak): ")
# if mandi == "ya":
#     waktu_hemat_mandi = 10
#     print("waktu yang dihemat 10 menit")
# else:
#     waktu_hemat_mandi = 0
#     print("waktu yang kamu perlukan 10 menit")

# kendaraan = input("kamu akan menggunakan kendaraan apa (sepeda/motor): ")
# if kendaraan == "sepeda":
#     waktu_kendaraan = 30
#     print("waktu yang digunakan 30 menit")
# else:
#     waktu_kendaraan = 15
#     print("waktu yang kamu perlukan 15 menit")

# total_waktu = waktu_hemat_makan + waktu_hemat_mandi + waktu_kendaraan
# print("Waktu yang anda gunakan adalah", total_waktu, "menit")

# if total_waktu > waktu_sampain_kampus:
#     print("Anda terlambat")
# elif total_waktu < waktu_sampain_kampus:
#     print("Anda tepat waktu")
# else:
#     print("Waktu Anda pas sampai di kampus")
# a = 24
# b = 36

# while b != 0:
#     a, b = b, a % b
# print(f"fpb-nya adalah:{a}")

nilai = str(input("masukkan nilai:"))
for i in range(1, 10+1):
        for j in range(1, 10+1):
            print(f"{i * j:4}", end=" ")
        print()


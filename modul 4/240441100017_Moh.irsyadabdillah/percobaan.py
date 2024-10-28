# # Input ukuran sisi belah ketupat dan karakter pilihan
# N = int(input("Masukkan ukuran sisi belah ketupat (N): "))
# karakter = input("Masukkan karakter untuk pola checkerboard (misalnya 'X' atau 'O'): ")

# # Perulangan untuk setiap baris dari 0 hingga 2*N - 2
# for i in range(2 * N - 1):
#     # Loop untuk mencetak karakter di setiap kolom
#     for j in range(2 * N - 1):
#         # Kondisi untuk menentukan apakah posisi (i, j) berada dalam belah ketupat
#         if abs(N - 1 - i) + abs(N - 1 - j) < N:
#             # Pola checkerboard dimulai dari tengah
#             if (i + j) % 2 == 0:
#                 print(karakter, end='')
#             else:
#                 print(' ', end='')
#         else:
#             print(' ', end='')
#     print()  # Pindah ke baris berikutnya
# Meminta input bilangan desimal dari pengguna
# Inisialisasi variabel
# Inisialisasi variabel
# gaji_harian = 100000
# maks_lembur_per_hari = 8
# batas_lembur_mingguan = 40

# total_gaji_reguler = 0
# total_gaji_lembur = 0
# total_jam_lembur = 0

# print("Masukkan jam lembur untuk 7 hari:")

# # Input jam lembur untuk setiap hari dan perhitungan lembur
# for hari in range(1, 8):
#     lembur = int(input(f"Jam lembur hari ke-{hari}: "))

#     # Validasi batas lembur harian
#     if lembur > maks_lembur_per_hari:
#         print("Lembur melebihi batas, tidak dihitung.")
#         lembur = 0

#     total_jam_lembur += lembur  # Akumulasi total jam lembur mingguan

#     # Cek batas lembur mingguan
#     if total_jam_lembur >= batas_lembur_mingguan:
#         print(f"Lembur hari ke-{hari} dihentikan karena melebihi batas mingguan.")
#         total_jam_lembur = batas_lembur_mingguan  # Set ke batas maksimal
#         break  # Keluar dari loop karena lembur dihentikan

#     # Hitung bonus lembur harian
#     if lembur == 0:
#         bonus_lembur = 0
#     elif lembur < 4:
#         bonus_lembur = lembur * 25000
#     elif lembur == 4:
#         bonus_lembur = 100000
#     elif lembur == 6:
#         bonus_lembur = 200000
#     elif lembur == 8:
#         bonus_lembur = 300000

#     total_gaji_lembur += bonus_lembur
#     print(f"Bonus lembur hari ke-{hari}: Rp{bonus_lembur:,}")

# # Hitung total gaji mingguan tanpa lembur dan dengan lembur
# total_gaji_reguler = gaji_harian * 7
# total_gaji_mingguan = total_gaji_reguler + total_gaji_lembur

# # Cetak hasil akhir
# print("\n--- Rincian Gaji Mingguan ---")
# print(f"Total lembur selama 7 hari: {total_jam_lembur} jam")
# print(f"Total gaji lembur: Rp{total_gaji_lembur:,}")
# print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_reguler:,}")
# print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan:,}")
# Inisialisasi variabel


# gaji_harian = 100000
# lembur_per_hari = []  # List untuk menyimpan jam lembur per hari
# total_lembur_seminggu = 0  # Menyimpan total jam lembur selama seminggu
# total_gaji_lembur = 0  # Menyimpan total gaji dari lembur

# # Input jam lembur selama 7 hari
# for hari in range(1, 8):  # 7 hari dalam seminggu
#     jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari}: "))
    
#     if jam_lembur > 8:
#         print("PERINGATAN !!! Lembur melebihi batas, tidak akan dihitung, ISTIRAHATLAH.")
#         jam_lembur = 8  # Batasi lembur maksimal 8 jam
#     lembur_per_hari.append(jam_lembur)
    
#     # Hitung total jam lembur selama seminggu
#     total_lembur_seminggu += jam_lembur

#     # Cek apakah total lembur sudah mencapai atau melebihi 40 jam
#     if total_lembur_seminggu >= 40:
#         print("Total lembur telah mencapai 40 jam, lembur dihentikan.")
#         lembur_per_hari[-1] = 40 - (total_lembur_seminggu - jam_lembur)
#         total_lembur_seminggu = 40
#         break

# # Menghitung gaji lembur harian dan total gaji lembur
# for jam_lembur in lembur_per_hari:
#     gaji_lembur_harian = 0  # Set default gaji lembur harian ke 0
    
#     # Menghitung gaji lembur berdasarkan jumlah jam lembur
#     if jam_lembur == 0:
#         gaji_lembur_harian = 0  # Tidak ada lembur
#     elif 1 <= jam_lembur < 4:
#         gaji_lembur_harian = 25000 * jam_lembur  # Rp25.000 per jam lembur untuk 1-3 jam
#     elif jam_lembur >= 4 and jam_lembur < 6:
#         gaji_lembur_harian = 100000  # Rp100.000 untuk 4 atau 5 jam lembur
#     elif jam_lembur >= 6 and jam_lembur < 8:
#         gaji_lembur_harian = 200000  # Rp200.000 untuk 6 atau 7 jam lembur
#     elif jam_lembur == 8:
#         gaji_lembur_harian = 300000  # Rp300.000 untuk 8 jam lembur

#     total_gaji_lembur += gaji_lembur_harian  # Tambahkan ke total gaji lembur

# # Menghitung gaji reguler mingguan dan total gaji mingguan termasuk lembur
# gaji_mingguan_tanpa_lembur = gaji_harian * 7
# total_gaji_mingguan = gaji_mingguan_tanpa_lembur + total_gaji_lembur

# # Cetak hasil perhitungan
# print("\nRingkasan:")

# for hari, jam_lembur in enumerate(lembur_per_hari, 1):
#     print(f"Lembur hari ke-{hari}: {jam_lembur} jam")

# print(f"Total lembur selama seminggu: {total_lembur_seminggu} jam")
# print(f"Total gaji lembur: Rp{total_gaji_lembur}")
# print(f"Total gaji mingguan tanpa lembur: Rp{gaji_mingguan_tanpa_lembur}")
# print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")

# jam=[4,5]

# for i in jam:
#     print(i)

# lembur_per_hari=[100000,200]

# for hari, jam_lembur in enumerate(lembur_per_hari, 1):
#     print(f"Lembur hari ke-{hari}: {jam_lembur} jam")
# Input dari pengguna
N = int(input("Masukkan ukuran sisi N: "))
karakter = input("Masukkan karakter pilihan (misal 'X' atau 'O'): ")

# Menghitung jumlah baris
total_baris = 2 * N - 1

# Loop untuk setiap baris
for i in range(total_baris):
    # Menentukan jumlah spasi di awal baris
    if i < N:
        spasi = N - i - 1
    else:
        spasi = i - N + 1

    # Membangun baris ketupat
    baris = "v"
    for j in range(total_baris):
        if (j >= spasi and j < total_baris - spasi) and ((i + j) % 2 == 0):
            baris += karakter
        else:
            baris += " "

    # Menampilkan baris
    print(baris)

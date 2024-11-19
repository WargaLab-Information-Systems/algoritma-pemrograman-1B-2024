# Menghitung gaji Mas Ironi

gaji_harian = 100000
max_lembur_seminggu = 40
max_lembur_perhari = 8

# Menghitung jam lembur 
lembur_perhari = 0
list_lembur_perhari = []
for i in range (7):
    jam_lembur = int(input(f"Berapa jam Mas Ironi lembur hari ke-{i+1}? "))
    lembur_perhari += jam_lembur
    list_lembur_perhari.append(jam_lembur)
    if jam_lembur > max_lembur_perhari:
        print("Lembur melebihi batas, tidak dihitung.")
    if lembur_perhari >= max_lembur_seminggu:
        print("Lembur dihentikan")
        break

# Menghitung gaji lembur
gaji_lembur = 0

for jam_lembur in (list_lembur_perhari):
    if jam_lembur == 4:
        gaji_lembur += 100000
    if jam_lembur == 6:
        gaji_lembur += 200000
    if jam_lembur == 8:
        gaji_lembur += 300000
    if jam_lembur == 3 or jam_lembur == 2 or jam_lembur == 1:
        gaji_lembur += jam_lembur * 25000

print("Jam lembur perhari : ", list_lembur_perhari)
print("Total lembur selama satu minggu adalah ", lembur_perhari)
print("Total gaji lembur Mas Ironi adalah Rp.", gaji_lembur)
print("Total gaji mingguan tanpa lembur adalah Rp.", gaji_harian * 7)
print("Total gaji mingguan termasuk lembur adalah Rp.", (gaji_harian * 7) + gaji_lembur)
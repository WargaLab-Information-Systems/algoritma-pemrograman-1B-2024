hari = 7
max_jam_lembur_hari = 8
max_jam_lembur_minggu = 40
jam_reguler = 12
gaji_per_hari = 100_000

boleh_lembur = True
lembur =  {
    "total"   : 0,
    "hari"    : 0,
}

gaji = {
    "total"         : 0,
    "reguler"       : 0,
    "lembur"        : 0,
    "tanpa_lembur"  : 0
}

def print_hasil():
  print("="*20)
  print("Gaji per harian :")
  print(f"Reguler : Rp.  {gaji['reguler']:>10,} | ")
  print(f"Lembur  : Rp.  {gaji['lembur']:>10,} | ")
  print("-"*20)
  print(f"Total   : Rp.  {gaji['total']:>10,} | ")
  print("="*20)
  print("Lembur : ")
  print(f"Lembur hari ini: {lembur['hari']} ")
  print(f"Total lembur sisa {max_jam_lembur_minggu - lembur['total']} jam" )

for i in range(1, hari + 1):
  print("="*20)
  print(f"Hari ke-{i}")
  jumlah_jam = int(input("jumlah jam : "))
  jam_lembur = jumlah_jam - jam_reguler

  gaji['total'] += gaji_per_hari
  gaji['reguler'] += gaji_per_hari

  if jam_lembur < 0:
    print("Tidak kerja sama dengan tidak makan")
    continue

  if jam_lembur == 0:
    gaji['tanpa_lembur'] += gaji_per_hari
    print_hasil()
    continue

  if lembur['total'] > max_jam_lembur_minggu:
    print_hasil()
    continue

  if jam_lembur > max_jam_lembur_hari:
    print("Lembur melebihi batas, tidak dihitung.")
    print_hasil()
    continue

  lembur["hari"] = jam_lembur
  lembur["total"] += jam_lembur

  if jam_lembur > 0 and jam_lembur < 4:
    total = 25_000 * jam_lembur
    gaji['lembur'] += total
    gaji['total'] += total
    lembur["hari"] += jam_lembur
  else:
    total = gaji_per_hari * ((jam_lembur - 4) // 2 + 1)
    gaji['lembur'] += total
    gaji['total'] += total
    lembur["hari"] += jam_lembur
  print_hasil()

print("\n\n\nTotal Gaji selema seminggu:")
print(f"Total Lembur seminggu: {lembur['total']} jam")
print(f"Total Gaji (lembur): Rp. {gaji['lembur']:,}")
print(f"Total Gaji (tanpa lembur): Rp. {gaji['tanpa_lembur']:,}")
print(f"Total Gaji (termasuk lembur): Rp. {gaji['total']:,}")
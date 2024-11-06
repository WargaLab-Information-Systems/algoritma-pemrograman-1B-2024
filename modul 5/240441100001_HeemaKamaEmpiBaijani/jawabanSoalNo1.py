def calculate_discount():
  total = int(input("total belanja anda: "))
  membership = str(input("jenis membership: "))
  membership_diskon = {
      "gold": 0.15,
      "silver": 0.1,
      "bronze": 0.05,
  }

  diskon = membership_diskon[membership] if membership in membership_diskon else 0

  if total >= 1_000_000:
    diskon += 0.05

  total_diskon = total * diskon
  jumlah_akhir = total - total_diskon
  print(f"total diskon setelah belanja: {total_diskon}")
  print(f"jumlah akhir keseluruhan: {jumlah_akhir}")

calculate_discount()
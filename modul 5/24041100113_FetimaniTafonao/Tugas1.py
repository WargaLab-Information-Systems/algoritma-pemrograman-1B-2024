def calculate_discount():
    while True:
        total_belanja = int(input("Masukkan total belanja: "))
        membership = input("Apakah kamu mempunyai kartu membership? (iya/tidak): ")
        diskon = 0
        if membership == "iya":
            kartu = input("Pilih membership anda: Gold/Silver/Bronze: ")
            if kartu == "Gold":
                diskon = 0.15
            elif kartu == "Silver":
                diskon = 0.10
            elif kartu == "Bronze":
                diskon = 0.05
            else:
                print("Harap masukkan kartu dengan benar!!!")
                continue
        if membership == "tidak":
            diskon = 0.0
            print("Anda tidak mendapatkan diskon")
        if total_belanja > 1000000:
            diskon += 0.05
            print("Karna anda berbelanja lebih dari 1 jt maka anda dapat diskon tambahan 5%")
        total = total_belanja * diskon
        after_diskon = total_belanja - total
        return total, after_diskon
total, after_diskon = calculate_discount()
print(f"Total diskon yang di dapat: Rp{total}")
print(f"Total yang harus di bayar: Rp{after_diskon}")
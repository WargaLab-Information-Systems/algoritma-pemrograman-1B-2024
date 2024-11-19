def calculate_discount(total_belanja, tipe_member):
    diskon = 0
    # Penyeleksian tipe member
    if tipe_member == "gold":
        diskon = 15
    elif tipe_member == "silver":
        diskon = 10
    elif tipe_member == "bronze":
        diskon = 5
    elif tipe_member == "tidak":
        diskon = 0
    else:
        raise ValueError("Masukkan tipe member yang tepat!")

    # Total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 5

    # Hitung total diskon
    total_diskon = (diskon / 100) * total_belanja
    total_akhir = total_belanja - total_diskon

    return total_akhir, total_diskon


while True :
    try:
        while True :
            total_belanja = int(input("Berapa total belanja Anda? : "))
            tipe_member = input("Apa tipe member Anda? (gold/silver/bronze/tidak): ").strip().lower()
            calculate_discount(total_belanja, tipe_member)
            print(calculate_discount(total_belanja, tipe_member))
            # total_akhir, total_diskon = calculate_discount(total_belanja, tipe_member)

            # print(f"Total belanja: {total_belanja}")
            # print(f"Diskon: {total_diskon:.2f}")
            # print(f"Jumlah yang harus dibayar: {total_akhir:.2f}")
            print()

            ulang_pengitungan = input("apakah anda ingin mengulang penghitungan anda? (y/n) : ")
            if ulang_pengitungan == "n" :
                print("terimakasih sudah berbelanjaaa")
                break
            print()
        break

    except ValueError as a:
        print(a)
        ulang = input("Apakah Anda ingin mengulang? (y/n) : ").strip().lower()
        if ulang == "n":
            print("program berhenti")
            break
        print()
def calculate_discount():
    while True:
        total_belanja = int(input("Masukkan total belanja: "))
        membership = input("Apakah mempunyai member? (ya/tidak): ")
        diskon = 0

        if membership == "ya":
            member = input("Pilih membership: Gold / Silver / Bronze: ")
            if member == "Gold":
                diskon = 0.15
            elif member == "Silver":
                diskon = 0.10
            elif member == "Bronze":
                diskon = 0.05

        if membership == "tidak":
            diskon = 0.0
            print("Tidak dapat diskon")

        if total_belanja > 1000000:
            diskon += 0.05
            print("Anda mendapatkan tambahan diskon 5%")

        total = total_belanja * diskon
        setelah_diskon = total_belanja - total

        return total, setelah_diskon

total, setelah_diskon = calculate_discount()
print(f"Total diskon: {total}")
print(f"Total yang harus dibayar: {setelah_diskon}")


while True:
    belanja_lagi = input("Apakah Anda ingin berbelanja lagi? (ya/tidak): ")
    if belanja_lagi == "ya":
        total, setelah_diskon = calculate_discount()
        print(f"Total diskon: {total}")
        print(f"Total yang harus dibayar: {setelah_diskon}")
    elif belanja_lagi == "tidak":
        print("Terima kasih sudah berbelanja!")
        break  


def halo_dunia(): 
print 'Halo Dunia!' 
halo_dunia() halo_dunia() 
# memanggil fungsi halo_dunia # fungsi halo_dunia dipanggil lagi 



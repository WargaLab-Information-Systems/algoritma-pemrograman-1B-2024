def calculate_discount():
    while True:
        total_belanja = int(input("Masukkan total belanja:"))
        membership = input("Apakah kamu mempunyai kartu membership? (iya / tidak) :")
        diskon = 0

        if membership == "iya":
            kartu = input("Pilih jenis membership anda : Gold / Silver / Bronze :")
            if kartu == "Gold":
                diskon = 0.15
            elif kartu == "Silver":
                diskon = 0.10 
            elif kartu == "Bronze":
                diskon = 0.05
            else :
                print("Harap masukkan jenis member yang sesuai")

        if membership == "tidak" :
            diskon = 0.0
            print("Anda tidak mendapatkan diskon")
        if total_belanja > 1000000:
            diskon +=0.05
            print("Selamat anda mendapatkan diskon tambahan sebesar 5% karena belanjaan anda melebihi 1 juta ")
                
        total = total_belanja * diskon
        after_diskon = total_belanja - total
        return total, after_diskon
    
total, after_diskon = calculate_discount ()
print(f"total diskon yang didapat : Rp{total}")
print(f"Total yang harus dibayar : Rp{after_diskon}")
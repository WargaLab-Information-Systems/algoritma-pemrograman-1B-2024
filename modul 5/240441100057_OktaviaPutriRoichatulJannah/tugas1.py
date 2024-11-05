def calculate_discount(tot_belanja,anggota):
    
    if anggota == "Gold":
        diskon = tot_belanja * 15/100
        stlh_diskon_anggota = tot_belanja - diskon
    elif anggota == "Silver":
        diskon = tot_belanja * 10/100
        stlh_diskon_anggota = tot_belanja - diskon 
    elif anggota == "Bronze":
        diskon = tot_belanja * 5/100
        stlh_diskon_anggota = tot_belanja - diskon   
    else:
        stlh_diskon_anggota = tot_belanja
                    
    if tot_belanja > 1000000:
        diskon_tambahan = stlh_diskon_anggota * 5/100
        harga_akhir = stlh_diskon_anggota - diskon_tambahan
        return harga_akhir
    else:
        return stlh_diskon_anggota

tot_belanja = int(input("Berapa total belanja pelanggan Rp. "))
anggota = input("Jenis kartu anggota yang dimiliki pelanggan : ")
while tot_belanja < 0:
    tot_belanja = int(input("Inputan salah! Masukkan nilai yang tidak minus :"))
    anggota = input("Jenis kartu anggota yang dimiliki pelanggan : ")

print(f"Harga setelah diskon adalah Rp. {calculate_discount(tot_belanja,anggota)}")
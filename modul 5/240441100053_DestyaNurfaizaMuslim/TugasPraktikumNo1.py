# calculate_discount()

def calculate_discount(anggota, total_belanja):
    diskon_keanggotaan = 0
    print("Total belanjaan anda adalah Rp. ",total_belanja)
    if anggota == "tidak punya":
        diskon_keanggotaan += 0
    else :
        if anggota == "gold":
            print("Selamat anda mendapatkan diskon 15%, karena memiliki keanggotaan Gold")
            diskon_keanggotaan += (15/100*total_belanja)
        if anggota == "silver":
            print("Selamat anda mendapatkan diskon 10%, karena memiliki keanggotaan Silver")
            diskon_keanggotaan += (10/100*total_belanja)
        if anggota == "bronze":
            print("Selamat anda mendapatkan diskon 5%, karena memiliki keanggotaan Bronze")
            diskon_keanggotaan += (5/100*total_belanja)

    total_setelah_diskon = total_belanja - diskon_keanggotaan

    if (total_belanja > 1000000):
        print("Selamat anda mendapatkan diskon 5%, karena berbelanja diatas 1 juta")
        diskon_tambahan = (5/100*total_belanja)
        total_setelah_diskon -= diskon_tambahan
    else:
        diskon_tambahan = 0
    
    return (total_setelah_diskon, diskon_keanggotaan, diskon_tambahan)
    
total_belanja = int(input("Berapa total belanjaan anda? : ")) 
while total_belanja < 0:
    total_belanja = int(input("Inputan anda salah. Masukkan harga diatas 0 : "))

anggota = input("Jenis keanggotaan apa yang anda miliki? (gold/silver/bronze/tidak punya) : ")
total_setelah_diskon, total_diskon, total_diskon_tambahan = calculate_discount(anggota, total_belanja)
print("Diskon yang anda dapat sebanyak Rp. ", int(total_diskon))
print("Total belanjaan anda adalah Rp. ", int(total_setelah_diskon) )
print("Diskon tambahannya adalah Rp. ", int(total_diskon_tambahan))
def calculate_discount(total_belanja, jenis_keanggotaan): #2 parameter
    diskon = 0
        
    #menentukan diskon berdasarkan jenis keanggotaan
    
    if jenis_keanggotaan.lower() == "gold":
        diskon = 0.15 #15%
    elif jenis_keanggotaan.lower() == "silver":
        diskon = 0.10 #10%
    elif jenis_keanggotaan.lower() == "bronze":
        diskon = 0.05 #5%
    else:
        diskon = 0.0 # tidak ada diskon jika tidak ada keanggotaan 
    
    
    if total_belanja > 1000000:
        diskon += 0.05 
     
    #menghitung total diskon
    total_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - total_diskon
    
    return total_diskon, total_setelah_diskon


#meminta input dari pengguna
total_belanja_input = float(input("masukkan total belanja: "))
if total_belanja_input <=1000:
    print("masukkan diatas 1000")
else:
    jenis_keanggotaan_input = input("masukkan jenis keanggotaan (gold/silver/bronze/tidak ada) ")

#menghitung diskon dan total setelah diskon
    total_diskon, total_setelah_diskon = calculate_discount(total_belanja_input, jenis_keanggotaan_input)

#menampilkan hasil
    print(f"total diskon: {total_diskon:.2f}")
    print(f"total setelah diskon: {total_setelah_diskon:.2f}") #menampilkan angka desimal dengan 2 angka diblkng koma
    
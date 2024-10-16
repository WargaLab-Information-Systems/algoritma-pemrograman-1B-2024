while False:
    angka_input = input("Silakan masukkan angka bulat : ")

    angka_balikan = ""
    for digit in angka_input:
        angka_balikan = digit + angka_balikan  
    
    print("Urutan angka yang dibalik:", angka_balikan)
    break

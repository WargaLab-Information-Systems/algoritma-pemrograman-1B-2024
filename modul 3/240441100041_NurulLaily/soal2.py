angka = input("Masukkan angka bulat: ")

angka_terbalik = ""

if angka.isdigit():
    angka_terbalik = ""
    for digit in angka:
        angka_terbalik = digit + angka_terbalik
    
    print("Angka setelah dibalikkan:", angka_terbalik)
else:
    print("Input bukan angka. Silahkan massukkan angka bulat!")

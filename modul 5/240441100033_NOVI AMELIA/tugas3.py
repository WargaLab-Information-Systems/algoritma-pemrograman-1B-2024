def faktorial(angka):
    # Basis: Jika n adalah 0 atau 1, kembalikan 1
    if angka == 0 or angka == 1:
        print(f"{angka}! = 1")
        return 1
    
    # Perulangan untuk menghitung faktorial sambil menampilkan proses perhitungannya
    hasil = 1                    #Variabel untuk menyimpan hasil faktorial
    proses = f"{angka}! = "     #menampilkan langkah faktorial secra berurutan
    
    for i in range(angka, 0, -1):
        hasil *= i
        proses += f"{i} x " if i > 1 else f"{i} = {hasil}" #jika angka lebih dari 1maka ditambah x
    
    print(proses)
    return hasil

# Contoh penggunaan
angka = int(input("Masukkan bilangan untuk dihitung faktorialnya: "))
faktorial(angka)
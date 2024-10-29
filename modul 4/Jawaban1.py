# input variabel 
d = int(input("Masukkan ukuran sisi belah ketupat : "))
k = input("Masukkan karakter yang Anda inginkan (X/O) : ")

if k == "X" or k== "O" :

# bagian atas belah ketupat 
    for i in range(d-1):
        for j in range(i,d): # spasi bagian kiri misal i = 0 bakal cetak 5 spasi
            print(' ',end=' ')
        for j in range(i): # karakter bagian kiri puncak misal i = 0 cetak 0 karakter
            print(k ,end=' ')
        for j in range(i+1): # karakter bagian kanan puncak misal i = 0 cetak 1 karakter
            print(k, end=' ')
        print()

    # bagian bawah belah ketupat 
    for i in range(d): 
        for j in range(i+1): # cetak spasi bagian kiri 
            print(' ', end=' ')
        for j in range(i, d-1): # cetak karakter bagian kiri 
            print(k, end=' ')
        for j in range(i,d): # cetak karakter bagian kanan 
            print(k, end=' ')
        print()

else:
    print("masukkan karakter kembali")

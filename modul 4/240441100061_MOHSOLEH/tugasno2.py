desimal = int(input("Masukkan bilangan desimal : "))

biner = "" # Menginisialisasi variabel biner sebagai string kosong
while desimal > 0: # Memulai loop yang akan terus berjalan selama desimal lebih besar dari 0 seperti 1
    biner = str(desimal % 2) + biner # Menghitung sisa dari desimal dibagi 2 yang akan menjadi digit biner
    desimal //= 2 # Mengupdate nilai desimal dengan membagi 2

panjang = len(biner) # Menentukan panjang karakter 
for i in range(1, panjang + 1): # Ini akan digunakan untuk mencetak setiap substring dari biner.
    print(biner[:i]) #yang memberikan efek "segitiga".
#menampilkan angka 1
for i in range (7):
    print("  x  ")


#menampilkan angka 4
for i in range(7):
    if i == 0:  # Baris pertama
        print("h     h")
    elif i in [1, 2]:  # Baris kedua dan ketiga
        print("x     x")
    elif i == 3:  # Baris keempat
        print("hhhhhhh")
    elif i in [4, 5]:  # Baris kelima dan keenam
        print("      x")
    else:  # Baris terakhir
        print("      x")
  
#Menampilkan angka 5
for i in range(7):
    if i == 0:  # Baris pertama
        print("hhhhhhh")
    elif i in [1, 2]:  # Baris kedua dan ketiga
        print("x      ")
    elif i == 3:  # Baris keempat
        print("hhhhhhh")
    elif i in [4, 5]:  # Baris kelima dan keenam
        print("      x")
    else:  # Baris terakhir
        print("hhhhhhh")
  
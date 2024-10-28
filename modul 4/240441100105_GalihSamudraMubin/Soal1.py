size = int(input("Masukkan Size Yang Anda Inginkan!! :"))

while True:
    karakter = str(input("Masukkan Karakter Yang Ingin Anda Tampilkan!! (X/O): "))
    if karakter == "X" or karakter == "O":
        break
    else :
        print("Input tidak Valid!!, Masukkan Karakter Yang Ingin Anda Tampilkan!! (X/O): ")

for i in range(size):
    print(' ' * (size - i - 1), end='') 
    for j in range(2 * i + 1):
        print(karakter if j % 2 == 0 else ' ', end='') 
    print()  

for i in range(size - 2, -1, -1):
    print(' ' * (size - i - 1), end='') 
    for j in range(2 * i + 1):
        print(karakter if j % 2 == 0 else ' ', end='')  
    print()  

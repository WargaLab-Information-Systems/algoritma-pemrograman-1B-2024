size = int(input("Massukkan Size :"))
# Menampilkan angka 1
for i in range(size):
         print(""*(size)+"x")
print()  

# Menampilkan angka 2
for i in range(size):
    if i == 0 or i ==size//2 or i == size-1:  
        print("hhhhhhh" )
    elif i < size//2: 
        print("      x") 
    elif i > size//2:  
        print("x      ")
    else:  
        print()

print()  

# Menampilkan angka 9
for i in range(size):
    if i == 0 or i ==size//2 or i == size-1:  #atas tengah dan bawah
        print("hhhhhhh")
    elif i < size//2: 
        print("x     x")
    else:  
        print("      x")
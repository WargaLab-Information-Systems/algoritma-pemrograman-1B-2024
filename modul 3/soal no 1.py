size = int(input("Masukkan size : "))

if size < 3:
    print("Size minimal 3 untuk pola yang benar.")
else:
    #angka 0
    print("x" * size)  
    for i in range(size-2):  
        print("n" + " " * (size - 2) + "x")
    print("h" * size)  
    print("")

    # Angka 2
    print("x" * size) 
    for i in range((size - 2) // 2):  
        print(" " * (size - 1) + "x")
    print("x" * size)  
    for i in range((size - 2) // 2):  
        print("x" + " " * (size - 1))
    print("x" * size)  
    print("")  


    #angka 5
    print("x" * size)  
    for i in range((size-2)//2):  
        print("x" + " " * (size - 1))
    print("n" * size)  
    for i in range((size-2)//2):  
        print(" " * (size - 1) + "i")
    print("h" * size)  
    print("")





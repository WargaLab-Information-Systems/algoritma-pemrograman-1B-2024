def faktorial(n):
    hasil = 1
    output = f"{n}! = "  
    
    for i in range(n, 0, -1):
        hasil *= i
        output += f"{i} x " if i > 1 else f"{i} = {hasil}"
    
    print(output)
    return hasil

n = int(input("Masukkan bilangan untuk menghitung faktorial: "))
faktorial(n)


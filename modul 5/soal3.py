def faktorial(n):
    if n < 0:
        return "faktorial tidak untuk bilangan negatif."
    elif n == 0 or n == 1:
        return f"{n}! = 1"
    else:
        hasil = 1
        hitung = ""
        for i in range(n, 0, -1):
            print(i)
            hasil *= i
            hitung += f"{i} x " if i > 1 else f"{i}"
        return f"{n}! = {hitung} = {hasil}"


# Input dari pengguna
while True:
    try:
        n = int(input("Masukkan bilangan : "))
        print(faktorial(n))
        break
    except ValueError:
        print("Mohon masukkan bilangan bulat yang valid.")
    print()

def faktorial(angka):
    faktorial = ""
    total_faktorial = 1

    for i in reversed(range(1, angka + 1)):
        if i != 1:
            faktorial += str(i) + " x "
        else:
            faktorial += str(i)
        
        total_faktorial *= i

    return f"{angka}! = {faktorial} = {total_faktorial}"

angka = int(input("Masukkan angka untuk di cek faktorial: "))
print(faktorial(angka))
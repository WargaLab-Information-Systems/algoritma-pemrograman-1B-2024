def faktorial(n):
    if n < 0:
        return "Nilai yang diinputkan haruslah angka positif"
    else:
        faktorial = 1
        susunan = ""
        for i in range(n, 0, -1):
            faktorial *= i
            susunan += str(i)
            if i > 1:
                susunan += " x "
        
        if n == 0:
            susunan = "1"

    hasil_susunan = f"{n}! = {susunan} = {faktorial}"
    return hasil_susunan
            


n = int(input("masukkan nilai faktorial: "))
print(faktorial(n))
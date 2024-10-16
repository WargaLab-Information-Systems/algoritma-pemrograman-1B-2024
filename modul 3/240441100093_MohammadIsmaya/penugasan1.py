
# Meminta input ukuran dari pengguna
ukuran = int(input("Masukkan Ukuran: "))

# NIM yang akan dicetak
nim = "093"

# Mencetak setiap digit dari NIM
for digit in nim: # mengiterasi melalui digit dalam string nim
    if digit == '0':
        for baris in range(ukuran):
            if baris == 0 or baris == ukuran - 1:
                print("x" * ukuran)
            else:
                print("x" + " " * (ukuran - 2) + "x")
        print()
    elif digit == '9':
        for baris in range(ukuran):
            if baris == 0 or baris == ukuran // 2 or baris == ukuran - 1:
                print("x" * ukuran)
            elif baris < ukuran // 2:
                print("x" + " " * (ukuran - 2) + "x")
            else:
                print(" " * (ukuran - 1) + "x")
        print()
    elif digit == '3':
        for baris in range(ukuran):
            if baris == 0 or baris == ukuran // 2 or baris == ukuran - 1:
                print("x" * ukuran)
            else:
                print(" " * (ukuran - 1) + "x")
        print()
    else:
        print("Digit tidak dikenal")
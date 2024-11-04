# Program untuk mencetak angka 187.

n = 7  # Ukuran pola

# Angka 1
print("Angka 1:")
i = 0
while i < n:
    j = 0
    while j < n:
        if j == n - 1:  # Garis vertikal di sisi kanan
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1

# Angka 8
print("\nAngka 8:")
i = 0
while i < n:
    if i == 0 or i == n//2 or i == n - 1:  # Baris atas, tengah, dan bawah
        print("*" * n)
    else:
        print("*" + " " * (n-2) + "*")  # Cetak bintang di sisi kiri dan kanan
    i += 1

# Angka 7
print("\nAngka 7:")
i = 0
while i < n:
    if i == 0:  # Baris atas penuh
        print("*" * n)
    else:  # Diagonal menurun dari kanan ke kiri
        # j = 0
        while j < n:
            if j == n - i - 1:
                print("*", end="")
                # break  # Menghentikan loop setelah mencetak bintang
            else:
                print(" ", end="")
            j += 1
        print()
    i += 1








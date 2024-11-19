# Input
N = int(input("Masukkan ukuran sisi (N): "))
karakter = input("Masukkan karakter (misalnya 'X' atau 'O'): ")

while karakter != 'X' and karakter != 'O':
    karakter = input("Masukkan karakter (misalnya 'X' atau 'O'): ")
# Bagian atas (termasuk garis tengah)
for i in range(N):
    print("*" * (N - i - 1), end="")    # Spasi

    for j in range(0, 2 * i + 1):       # Pola
        if j % 2 == 0 :
            print(karakter, end="")
        else :
            print(" ", end="")
    print()

# # Bagian bawah
# for i in range(N - 2, -1, -1):
#     print(" " * (N - i - 1), end="")    # Spasi 

#     for j in range(0, 2 * i + 1):       # Pola
#         if j % 2 == 0 :
#             print(karakter, end="")
#         else :
#             print(" ", end="")
#     print() 
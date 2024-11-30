def cek_palindrom(kata):
    # Mengubah kata menjadi lowercase 
    kata = kata.lower()
    
    # kata[::-1] akan membalik urutan string
    if kata == kata[::-1]:
        return True
    else:
        return False

while True:
    # Input kata 
    kata_input = input("Masukkan kata yang ingin dicek (ketik 'selesai' untuk berhenti): ")
    
    if kata_input.lower() == 'selesai':
        print("Program selesai!")
        break
    
    # Memanggil fungsi cek_palindrom dan menampilkan hasilnya
    if cek_palindrom(kata_input):
        print(f"'{kata_input}' adalah palindrom")
    else:
        print(f"'{kata_input}' bukan palindrom")
    print()
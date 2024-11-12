def cek_palindrom(kata):
    # Membalikkan string
    palindrom = kata[::-1]
    # Membandingkan kata dengan kebalikannya
    if kata == palindrom:
        return "palindrom"
    else:
        return "bukan palindrom"

# Contoh penggunaan
kata = 'kasur rusak'
hasil = cek_palindrom(kata)
print(hasil)  # Output: bukan palindrom

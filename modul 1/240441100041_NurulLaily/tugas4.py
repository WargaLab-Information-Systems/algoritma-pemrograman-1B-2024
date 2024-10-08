n = 7 # total orang
r = 4 # orang yang dipilih

# Menghitung banyak cara untuk memilih r orang dari n orang
jumlah_cara = (n * (n-1) * (n-2) * (n-3) // (1*2*3*4))

print(f"Banyak cara untuk membentuk tim dari {n} orang dengan memilih {r} orang adalah: {jumlah_cara}")
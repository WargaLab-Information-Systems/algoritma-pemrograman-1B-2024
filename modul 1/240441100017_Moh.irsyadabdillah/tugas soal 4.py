n = 7  # Total orang
k = 4  # Orang yang dipilih

# Menghitung faktorial
faktorial_n = 7 * 6 * 5 * 4 * 3 * 2 * 1

faktorial_k = 4 * 3 * 2 * 1

faktorial_nk = 3 * 2 * 1

# Menghitung kombinasi C(n, k) = n! / (k! * (n-k)!)
kombinasi = faktorial_n // (faktorial_k * faktorial_nk)

# hasil
print("")
print(f"Rumus mencari kombinasi: faktorial_n // (faktorial_k * faktorial_nk)")
print("")
print(f"faktorial n / 7! adalah {faktorial_n}")
print(f"faktorial k / 4! adalah {faktorial_k}")
print(f"faktorial nk / 3! adalah {faktorial_nk}")
print("")
print(f"kombinasi = {faktorial_n} // ({faktorial_k} * {faktorial_nk}) = {kombinasi}")
print(f"Jumlah cara untuk memilih {k} orang dari {n} orang adalah: {kombinasi}")
print("")
# input nama dan nim
nama = input("Masukkan Nama ")
nim = input("Masukkan NIM ")

# input nilai
nilaiuts = int(input("Masukkan nilai UTS: "))
nilaiuas = int(input("Masukkan nilai UAS: "))

print(f"Masukkan nama {nama}")
print(f"NIM Anda: {nim} ")

# menghitung nilai rata-rata
hasil_ratarata = (nilaiuts + nilaiuas) / 2
print(f"Rata-rata nilai Anda adalah {hasil_ratarata}")

# menggunakan if elif else
if 100 >= hasil_ratarata >= 81:
    print("Anda mendapatkan nilai A")
elif 80 >= hasil_ratarata >= 71:
    print("Anda mendapatkan nilai B")
elif 70 >= hasil_ratarata >= 61:
    print("Anda mendapatkan nilai C")
elif 60 >= hasil_ratarata >= 41:
    print("Anda mendapatkan nilai D")
elif 40 >= hasil_ratarata >= 0:
    print("Anda mendapatkan nilai E")
else:
    print("Tetap semangat!! selamat mencoba lagi")
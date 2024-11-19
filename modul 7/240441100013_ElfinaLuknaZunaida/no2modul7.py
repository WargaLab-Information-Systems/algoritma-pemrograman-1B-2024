klub_basket = {"Mail", "Yaya", "Fizi", "Ehsan", "Zul"}
klub_renang = {"Yaya", "Ying", "Gopal", "Fang", "Zul"}


print("Klub Basket:", klub_basket)
print("Klub Renang:", klub_renang)
print("Siswa yang mengikuti kedua klub:", klub_basket & klub_renang)
print("Siswa yang hanya mengikuti satu klub:", klub_basket ^ klub_renang)
print("Daftar semua siswa unik yang mengikuti setidaknya satu klub:", klub_basket | klub_renang)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", len(klub_basket | klub_renang))

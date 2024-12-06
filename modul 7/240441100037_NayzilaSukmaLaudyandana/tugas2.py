anggota = {
    "klub_basket": {"ipin", "mail", "devi", "ijat", "susanti"},
    "klub_renang": {"ijat", "jarjit", "fizi", "ehsan", "memei"}
}

klub_basket = anggota["klub_basket"]  
klub_renang = anggota["klub_renang"] 

kedua_klub = klub_basket & klub_renang 
print("\nSiswa yang mengikuti kedua klub:")
print(kedua_klub)

hanya_satu_klub = klub_basket ^ klub_renang 
print("\nSiswa yang mengikuti satu klub:")
print(hanya_satu_klub)

semua_siswa = klub_basket | klub_renang 
print("\nDaftar semua siswa unik yang mengikuti setidaknya satu klub:")
print(semua_siswa)

jumlah_siswa_unik = len(semua_siswa) 
print("\nJumlah siswa unik yang mengikuti setidaknya satu klub:")
print(jumlah_siswa_unik)

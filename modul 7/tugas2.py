
klub_basket = {"okta","via","putri","puput","icha"}
klub_renang = {"adit","puput","dayat","icha","chilmi","tiar"}
print(f"siswa yang mengikuti klub basket adalah {klub_basket}")
print(f"siswa yang mengikuti klub renang adalah {klub_renang}")

print("="*30)
ikut_dua_klub = klub_basket & klub_renang
print(f"siswa yang mengikuti kedua klub adalah {ikut_dua_klub}")

print("="*30)
ikut_basket_saja = klub_basket - klub_renang
print(f"Siswa yang hanya ikut klub basket saja adalah {ikut_basket_saja}")
ikut_renang_saja = klub_renang - klub_basket
print(f"Siswa yang hanya ikut klub renang saja adalah {ikut_renang_saja}")
ikut_satu_klub = ikut_basket_saja | ikut_renang_saja
print(f"Siswa yang hanya mengikuti satu klub saja adalah {ikut_satu_klub}")

print("="*30)
semua_siswa = klub_basket | klub_renang
print(f"Semua data siswa = {semua_siswa}")

print("="*30)
jumlah_siswa = len(semua_siswa)
print(f"Jumlah semua siswa adalah {jumlah_siswa}")
# Jaka skor 1100 dengan nilai ipk 3.5
# Ida skor 1000 dengan nilai ipk 3.5

# Input
nama1 = str(input("masukan nama pertama :"))
skor1 = int(input("masukan skor pertama :"))
ipk1 = float(input("masukan ipk pertama :"))

nama2 = str(input("masukan nama kedua :"))
skor2 = int(input("masukan skor kedua :"))
ipk2 = float(input("masukan ipk kedua :"))

# Penjelasan variabel
ketentuan_skor = 1100
ketentuan_ipk = 3.0

# Penyeleksian kondisi
if skor1 > ketentuan_skor and ipk1 >= ketentuan_ipk :
    print(f"{nama1} lolos persyaratan beasiswa")
else :
    print(f"{nama1} tidak lolos")

if skor2 > ketentuan_skor and ipk2 >= ketentuan_ipk :
    print(f"{nama2} lolos persyaratan beasiswa")
else :
    print(f"{nama2} tidak lolos")
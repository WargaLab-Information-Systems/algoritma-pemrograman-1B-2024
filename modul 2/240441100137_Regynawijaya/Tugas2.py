# Program dinamis untuk menentukan siapa yang lulus persyaratan beasiswa

# Syarat beasiswa
minimal_skor = 1100
minimal_ipk = 3.0

# Input data untuk Mahasiswa 1
nama1 = input("Masukkan nama Mahasiswa 1: ")
skor1 = float(input(f"Masukkan skor {nama1}: "))
ipk1 = float(input(f"Masukkan IPK {nama1}: "))

# Input data untuk Mahasiswa 2
nama2 = input("Masukkan nama Mahasiswa 2: ")
skor2 = float(input(f"Masukkan skor {nama2}: "))
ipk2 = float(input(f"Masukkan IPK {nama2}: "))

# Mengecek kelulusan Mahasiswa 1
if skor1 > minimal_skor and ipk1 >= minimal_ipk:
    print(f"{nama1} lulus persyaratan beasiswa.")
else:
    print(f"{nama1} tidak lulus persyaratan beasiswa.")

# Mengecek kelulusan Mahasiswa 2
if skor2 > minimal_skor and ipk2 >= minimal_ipk:
    print(f"{nama2} lulus persyaratan beasiswa.")
else:
    print(f"{nama2} tidak lulus persyaratan beasiswa.")
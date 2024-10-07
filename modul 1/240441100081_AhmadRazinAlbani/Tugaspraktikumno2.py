#NO2
#MENGHITUNG JUMLAH NILAI DARI 8 SUKU PERTAMA

def JumlahNilaiSuku(a, b, n):
    return n * (2 * a + (n-1) * b) / 2

#data di soal
#a5 = 11
#a8_tambah_a12 = 52
#menentukan nilai a dan b
#memakai rumus suku ke-n => an = a+(n-1)b
# a5 = a+4b
# 11 = a+4b

# a8 + a12 = 52
# (a+7b)+(a+11b) = 52
# 2a+18b = 52

#menyelesaikan persamaan
# a+4b = 11 => a = 11-4b
# 2a+18b = 52
# 2(11-4b)+18b = 52
# 22-8b+18b = 52
b = 3
# b=3 => a+4(3) = 11
a = -1
#menghitung jumlah nilai dari 8 suku pertama
n = 8
JumlahNilai = JumlahNilaiSuku(a, b, n)
print(f"Jumlah nilai dari 8 suku pertama dari deret aritmatika adalah {JumlahNilai}")

#1 menhitun volume balok dan tabung menghitung volume balok
# Menghitung folume balok
p = float(input("Maukkan panjang balok : "))
l = float(input("Masukkan tinggi balok: "))
t = float(input("Masukkan lebar balok: "))
volumebalok = p*l*t
print(volumebalok)

#menghitung volume tabung
import math

def volume_tabung(jari_jari, tinggi):
    volume = math.pi * jari_jari**2 * tinggi
    return volume

# Input jari-jari dan tinggi
r = float(input("Masukkan jari-jari alas tabung (dalam satuan cm): "))
t = float(input("Masukkan tinggi tabung (dalam satuan cm): "))

# Menghitung volume
volume = volume_tabung(r, t)

# Output volume
print(f"Volume tabung adalah {volume:.2f} cm³")

#2 menyelesaikan tugas keinintahuan darmaji
#Input nilai dari suku ke-5 dan jumlah suku ke-8 dan ke-12
sk_5 = float(input("Nilai suku ke-5: "))  # Misalnya, 11
sk_8_12 = float(input("Jumlah nilai suku ke-8 dan suku ke-12: "))  # Misalnya, 52

b = (sk_8_12 - 2 * sk_5) / 10
a = sk_5 - 4 * b

# Fungsi untuk menghitung jumlah n suku pertama dari deret aritmatika
def jumlah_deret_aritmatika(a, b, n):
    return (n / 2) * (2 * a + (n - 1) * b)

# Menghitung jumlah 8 suku pertama
n = 8
jumlah_8_suku_pertama = jumlah_deret_aritmatika(a, b, n)

# Output hasil
print(f"\nSuku pertama (a) = {a:.2f}")
print(f"Beda (b) = {b:.2f}")
print(f"Jumlah 8 suku pertama dari deret aritmatika tersebut adalah {jumlah_8_suku_pertama:.2f}")

#3 menghitun dolar ke rupiah
#Fungsi untuk menghitung konversi dari USD ke IDR
def konversi_dolar_ke_rupiah(dolar, nilai_tukar):
    return dolar * nilai_tukar

# Input dari pengguna: jumlah Dolar dan nilai tukar
dolar = float(input("Masukkan jumlah Dolar (USD): "))
nilai_tukar = float(input("Masukkan nilai tukar USD ke IDR : "))

# Menghitung konversi
rupiah = konversi_dolar_ke_rupiah(dolar, nilai_tukar)

# Output hasil
print(f"{dolar} USD setara dengan {rupiah:,.2f} IDR")

#4 Menghitun berapa banyak cara untuk mandor membentuk tim
import math

# Input dari pengguna
jumlah = int(input("Mandor memiliki tim berjumlah: "))  # Total anggota tim
dipilih = int(input("Dan mandor ingin memilih orang dari tim: "))  # Jumlah yang ingin dipilih

# Pastikan input valid
if dipilih > jumlah:
    print("Jumlah yang ingin dipilih tidak boleh lebih dari total anggota tim.")
else:
    # Menghitung kombinasi C(n, r)
    kombinasi = math.factorial(jumlah) // (math.factorial(dipilih) * math.factorial(jumlah - dipilih))
    
    # Output hasil
    print(f"Jumlah cara untuk memilih {dipilih} orang dari {jumlah} orang adalah: {kombinasi}")


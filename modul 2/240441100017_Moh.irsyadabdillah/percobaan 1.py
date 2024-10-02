# nama = input("nama anda siapa? ")

# if nama=="irsyad":
#     print("hai ganteng ")
# elif nama == "rizal":
#     print("hai si rizal ")
# else:
#     print("au ah gak kenal :(")

# print(f"akhir dari program")
# print(20*"=")
# print("kalkulator sederhana")
# print(20*"=" +"\n")

# angka_1 = float(input("masukkan angka 1 ="))
# operator = input("operator (+,-,x,/):")
# angka_2 = float(input("masukkan angka 2 = "))

# if operator == "+":
#     hasil = angka_1 + angka_2
#     print(f"hasilnya adalah {hasil}")
# elif operator == "-":
#     hasil = angka_1 - angka_2
#     print(f"hasilnya adalah {hasil}")
# elif operator == "x" or operator == "*":
#     hasil = angka_1 * angka_2
#     print(f"hasilnya adalah {hasil}")
# elif operator == "/":
#     hasil = angka_1 / angka_2
#     print(f"hasilnya adalah {hasil}")
# else :
#     print("masukkan yang bener dong!, aku pusing :(")
# print("akhir dari program, terima kasih ")
Nama = input("masukkan Nama =")
NIM =int(input("masukkan NIM ="))
nilai_UTS =int(input("masukkan nilai UTS ="))
nilai_UAS =int(input("masukkan nilai UAS ="))

print(f"mahasiswa atas nama {Nama} ")
print(f"nim anda {NIM} ")

rata_rata = (nilai_UTS + nilai_UAS) / 2
print("nilai rata-ratanya adalah: ",rata_rata,)

if rata_rata <= 40:
    print("anda mendapatkan nilai E")
elif rata_rata <= 60:
    print("anda mendapatkan nilai D")
elif rata_rata <= 70:
    print("anda mendapatkan nilai C")
elif rata_rata <= 80:
    print("anda mendapatkan nilai B")
elif rata_rata <=100:
    print("anda mendapatkan nilai A")
else:
    print("nilai yang ada masukkan lebih dari 100 coba input ulang")

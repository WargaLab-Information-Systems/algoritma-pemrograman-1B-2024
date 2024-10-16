# input data
skorJaka = 1100
ipkJaka = float(3.5)
skorIda = 1000
ipkIda = float(3.5)
minSkor = 1100
minIpk = float(3.0)

Jaka = "Jaka lulus persyaratan" if skorJaka >= minSkor and ipkJaka >= minIpk else "Jaka tidak lulus persyaratan"
print(Jaka)

Ida = "Ida lulus persyaratan" if skorIda >= minSkor and ipkIda >= minIpk else "Ida tidak lulus persyaratan"
print(Ida)
# input data
nama1 = "Jaka"
nama2 = "Ida"
skorNama1 = 1100
ipkNama1 = float(3.5)
skorNama2 = 1000
ipknama2 = float(3.5)
minSkor = 1100
minIpk = float(3.0)

# menentukan persyaratan beasiswa
if nama1 == "Jaka":
    if skorNama1 >= minSkor and ipkNama1 >= minIpk:
        print(f"{nama1} lulus persyaratan")
    else:
        print(f"{nama1} tidak lulus persyaratan")
        
if nama2 == "Ida":
    if skorNama2 >= minSkor and ipknama2 >= minIpk:
        print(f"{nama2} lulus persyaratan")
    else:
        print(f"{nama2} tidak lulus persyaratan")
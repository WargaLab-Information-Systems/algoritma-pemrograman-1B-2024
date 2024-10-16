play = True
while play:
    inp_hari = int(input("Masukan Hari : "))
    modulo_5 = inp_hari // 5 
    hari_biasa = inp_hari - 4
    denda = 2500 * (hari_biasa - (modulo_5 - 1)) if hari_biasa > 0 else 0
    
    if modulo_5 >=1:
        denda += 5500 * (modulo_5 - 1)
    print(denda)

    tanya = input("Apakah ingin melanjutkan? (y/n) : ")
    if tanya == "n":
        play = False 
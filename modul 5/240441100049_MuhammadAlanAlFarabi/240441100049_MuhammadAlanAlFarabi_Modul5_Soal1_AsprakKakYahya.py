def kalkulator_diskon(total, member):

    if member == 'Gold':
        diskon = 15/100
    elif member == 'Silver':
        diskon = 10/100
    elif member == 'Bronze':
        diskon = 5/100
    else:
        diskon = 0/100

    if total > 1000000:
        diskon += 5/10


    
    total_diskon = total * diskon
    return total_diskon


print("Selamat datang di Supermarket")
total = int(input("Berapa total belanja anda: "))
if total < 0:
    print("masukan di atasnya 0")
else:
    print("Apakah anda memiliki kartu member?(Gold, Silver, Bronze, none)")
    member = str(input("Jawaban anda: "))
    while member != "Gold" and member != "Silver" and member != "Bronze" and member != "None":
        print("Apakah anda memiliki kartu member?(Gold, Silver, Bronze, None)")
        member = str(input("Jawaban anda: "))


    dapat_diskon = kalkulator_diskon(total, member)
    total_diskon = total - dapat_diskon
    print(f"Diskon yang didapat: {dapat_diskon}")
    print(f"Anda harus membayar: {total_diskon}")
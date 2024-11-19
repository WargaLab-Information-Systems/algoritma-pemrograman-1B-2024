
discount = 0
def calculate_discount() :
    global discount
    member = str(input("Apakah kamu memiliki member? (yes/no)"))
    if member == "yes" :
        jenis_kartu = str(input("jenis kartu apa yang kamu miliki? (gold/silver/bronze)"))
        if jenis_kartu == "gold" :
                discount += 15
        if jenis_kartu == "silver" :
                iscount += 10
        if jenis_kartu == "bronze" :
                discount += 5
    total_belanja = int(input("Berapa total belanja anda?"))
    if total_belanja > 1000000 :
        discount += 5
    banyak_discount = total_belanja * discount / 100
    global bill
    bill = total_belanja- banyak_discount
    return discount
print("discount yang anda dapat adalah :", calculate_discount(),"%")
print("bill yang diterima adalah ",bill)
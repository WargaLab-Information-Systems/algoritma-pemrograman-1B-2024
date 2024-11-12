totalBelanja = int(input("Masukkan total belanja: "))
tandaAnggota = input("Apakah anda memiliki tanda anggota? [y/n] ")
kartuAnggota = ''
diskon = 0
if tandaAnggota=='y':
    kartuAnggota= input('masukan kartu anggota anda [gold/siver/bronze]: ')
else:
    print('anda tidak memiliki kartu anggota')



def hitungDiskon(totalBelanja, kartuAnggota,diskon):
    if tandaAnggota =='y':
        if kartuAnggota == "gold":
            diskon += 15/100
        elif kartuAnggota == "silver":
            diskon += 10/100
        elif kartuAnggota == "bronze":
            diskon += 5/100
    
    
    if totalBelanja > 1_000_000:
        diskon +=5/100

    totalDiskon= totalBelanja*diskon
    totalSetelahDiskon= totalBelanja-diskon
    return totalDiskon, totalSetelahDiskon
totalDiskon, totalSetelahDiskon = hitungDiskon(totalBelanja, kartuAnggota, diskon)

print(f'total belanja anda adalah', {totalBelanja})
print(f'total diskon anda adalah', {totalDiskon})
print(f'total belanja anda setelah diskon adalah',{totalSetelahDiskon} )



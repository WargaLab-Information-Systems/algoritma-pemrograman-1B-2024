#tahun dari user
tahun = int(input("Tahun berapa ini?")) 

#taun kabisan harus habis dibagi 4 
if tahun % 4 == 0 :  
    print(f"{tahun} adalah tahun kabisat")
else: 
    print(f"{tahun} bukan tahun kabisat")
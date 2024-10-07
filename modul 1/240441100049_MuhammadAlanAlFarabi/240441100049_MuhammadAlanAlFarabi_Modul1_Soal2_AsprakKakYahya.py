# Soal 2
print("soal no 2")
print("mencari suku ke 8")
# di ketahui suku ke 5 adalah 11
# di ketahui suku ke 8 dan suku ke 12 adalah 52
# berapakah suku ke 8

# U5 = a + (5-1) * b hasilnya a = 11-4b

# U8 + U12 = (a+(8-1)b) + (a+(12-1)b)
#          = (a+7b) + (a+11b)
#          = 2a + 18b
# dan hasil dari a = 26-9b

# bila seudah diketahui sepeti ini kita bisa mengitung a dan b
# b

rumusb = (26-11)/(9-4)
b     = rumusb 
print("nilai b adalah ", b)

# untuk nilai b sudah di ketahui, sekarang mencari nilai a
rumusa = 11-4*(3) 
# 3 adalah hasil dari b yang sebelumnya udah kita hitung
a     = rumusa
print("nilai a adalah ", a)
    
# sekarang kita aplikasikan nilai a dan nilai b untuk mencari suku ke 8
n   = 8
rumusn  = (n/2)*(2*a+(n-1)*b)
print("jadi suku ke 8 adalah", rumusn)
#  ditanya = jumlah nilai dari 8 suku pertama (S8) 
# rumus jumlah deret matematika Sn = 1/2 n (2a+(n-1)b)

# baris aritmatika suku n ke_5 = 11
# Un = a + (n-1)b #rumus  nilai suku ke n
# 11 = a + (5-1) b
# 11 = a + 4b # persamaan 1 

# U8 dan U12 
# U8 = a + (8-1)b
# U8 = a + 7b #persamaan 2

# U12 = a + 11b # persamaan 3

# U8+U12 = 52 
# a+7b+a+11b = 52
# 2a+18b = 52 #persamaan 4

# dari persamaan 1 
# 11 = a + 4b
# a = 11 - 4b # persamaan 5 

# persamaan 5 masuk ke persamaan 4 krn mencari b
# 2a+18b = 52
# 2(11-4b) + 18b = 52
# 22-8b + 18b =52
# 22+10b =52
# 10b =52-22
# 10b =30
# b=30/10
# b=3

# a = 11 - 4b # ke persamaan 5
# a = 11 - 4*3
# a = 11 - 12
# a = -1

# Sn = 1/2 n (2a+(n-1)b)
# S8 = 1/2 8 (2*(-1)+(8-1)3)
# S8 = 4 (-2+21)
# S8 = 4 (19)
# S8 = 76

# input
n = 8
a = -1
b = 3

# deret matematika
Sn = 1/2*n*(2*a+(n-1)*b)

# output 
print("hasil jumlah deret ke-8 = ", Sn)
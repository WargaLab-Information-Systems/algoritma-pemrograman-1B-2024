size = int(input("Masukkan size"))
for i in range (1,size+1,1) :
   if i < size+1 :
    print(" " * (size // 2)+"*" + " "*(size // 2))

for i in range (1,size + 1,1):
    if i == 1 :
        print("*" * size)
    if i <= size // 2 - 1 :
        print(" "* (size-1) + "*")
    if i == size//2 :
        print("*" * size)
    if i > size // 2 + 1:
        print("*")
    if i == size:
        print("*" * size)

for i in range (1, size + 1,1) :
    if i == 1 :
        print("*" * size)
    if i <= size // 2 - 1:
        print("*")
    if i == size // 2 :
        print("*" * size)
    if i > size // 2 + 1 :
        print(" " * (size-1) + "*")
    if i == size :
        print("*" * size)



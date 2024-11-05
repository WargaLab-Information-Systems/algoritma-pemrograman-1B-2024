n = 5

for wadah in range(n):
    if wadah == 0 or wadah == 4:
        print("x " * 5 )
    else:
        print("x " + " " *6 + "x")

print(" ")

for wadah in range (n):
    if wadah == 0 or wadah == 2 or wadah == 4:
        print("x "*5)
    else:
        if wadah == 1:
            print(" "*8 + "x ")
        else:
            print("x " + " "*8)

print(" ")

for wadah in range (n):
    if wadah == 0 or wadah == 2 or wadah == 4:
        print("x "*5)
    else:
        if wadah == 1:
            print("x " + " "*6 + "x " )
        else:
            print(" "*8 + "x ")

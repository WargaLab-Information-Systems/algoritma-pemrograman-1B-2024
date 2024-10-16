# #number NIM
def nol(n):
    print("* " * n)
    for i in range(n - 2):
        print("*" + "  " * (n - 2) + " " + "*")
    print("* " * n)


def satu(n):
    for i in range(n):
        print("  " * (n - 1) + "*")


def printAngka(inp = "", fontSize = 5):
    nums = {
        "0": nol,
        "1": satu,
    }

    for num in inp:
        nums[num](fontSize)
        print()

angka = input("Masukan Angka : ")
fontSize = int(input("Masukan Font Size : "))
printAngka(angka, fontSize)

size = int(input("Masukkan size: "))
rumus = int(size/2)

for i in range(size):
    print(" " * (size -5)+"x")
print()

print("x" * size)
for i in range(1, rumus):
    print("x" + " " * (size -2) + "x")
for i in range(1, rumus):
    print("x" + " " * (size -2) + "x")
print("x" * size)
print()

print("x" * size)
for i in range(2, rumus):
    print("x" + " " * (size -2) + "x")
print("x" * size)
for i in range(1, rumus):
    print(" " * (size -1) + "x")
print("x" * size)
# Fungsi untuk menghitung faktorial suatu bilangan

# menghitung faktorial
def factorial (n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n-1)

def step(n):
    step = []
    for i in range (n, 0,-1):
        step.append(str(i)) 
    step = " " "x" " " . join(step)
    return step
    
n = int(input("Masukkan angka : "))
print("angka faktorial ke", n,"adalah ", factorial(n))
if n == 0:
    print(f"{n}! = {factorial(n)}")
else:
    print(f"{n}! = {step(n)} = {factorial(n)}")
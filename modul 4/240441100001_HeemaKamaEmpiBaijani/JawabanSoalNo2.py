num = 999
def my_biner(inp):
  num = inp
  biner = ""
  i = 0
  while True:
    modulus = num % 2
    biner = str(modulus) + biner
    print(f"digit ke-{i:>3}, angka {num:>5} ", biner)
    num = num // 2
    if num == 0:
      break
    i+=1
  return biner

print(f"\nangka biner dari {num} adalah", my_biner(num))

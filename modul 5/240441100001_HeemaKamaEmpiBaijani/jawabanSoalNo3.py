def faktorial(n, s=""):
  if n <= 1: #basis
    s += "1"
    return 1, s
  s += str(n) + " x " 
  new_n, s = faktorial(n-1, s)
  return new_n * n, s
  
result, s = faktorial(5)
print("5! =", s, "=", result)
result, s = faktorial(3)
print("3! =", s, "=", result)
result, s = faktorial(2)
print("2! =", s, "=", result)
result, s = faktorial(0)
print("0! =", result)
# result, s = faktorial()s
# print("10! =", s, "=", result)
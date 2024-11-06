def isPalindrome(s):
  while len(s):
    if s[0] != s[-1]:
      return False
    s = s[1:-1]
  return True

a = "kakak"
result = isPalindrome(a)
print(a, result)

b = "ayam"
result = isPalindrome(b)
print(b, result)
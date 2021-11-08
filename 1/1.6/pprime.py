"""
ID: jujumoh1
LANG: PYTHON3
TASK: pprime
"""

import math, time

t = time.time()

fin = open('pprime.in', 'r')
fout = open('pprime.out', 'w')

a, b = fin.readline().strip().split()
palindromes = []

def find_palindromes(l, is_first=False):
  return_list = []
  if is_first:
    for i in range(1, 10, 2):
      if l > 2:
        palindromes.extend([i * pow(10, l - 1) + pal * 10 + i 
                for pal in find_palindromes(l - 2) 
                if int(a) <= i * pow(10, l - 1) + pal * 10 + i <= int(b)])
      else:
        if l == 2:
          if int(a) <= i * 10 + i <= int(b):
            palindromes.append(i * 10 + i)
        else:
          if int(a) <= i <= int(b):
            palindromes.append(i)
  elif l > 2:
    for i in range(10):
      return_list.extend([i * pow(10, l - 1) + pal * 10 + i 
                          for pal in find_palindromes(l - 2)])
  else:
    for i in range(10):
      if l == 2:
        return_list.append(i * 10 + i)
      else:
        return_list.append(i)
  return return_list

for i in range(len(a), len(b) + 1):
  find_palindromes(i, is_first=True)

for palindrome in palindromes:
  for i in range(3, math.isqrt(int(palindrome)) + 1, 2):
    if palindrome % i == 0: break
  else:
    fout.write(f'{palindrome}\n')

fin.close()
fout.close()

print(time.time() - t)
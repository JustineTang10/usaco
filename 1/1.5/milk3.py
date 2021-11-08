"""
ID: jujumoh1
LANG: PYTHON3
TASK: milk3
"""

import copy

fin = open('milk3.in', 'r')
fout = open('milk3.out', 'w')

a, b, c = [int(i) for i in fin.readline().strip().split()]
limits = [a, b, c]
milk_amounts = set()
calculated = []
milk_amounts.add(c)

def pour_milk(from_index, to_index, milk):
  if milk[to_index] + milk[from_index] <= limits[to_index]:
    milk[to_index] += milk[from_index]
    milk[from_index] = 0
  else:
    milk[from_index] -= limits[to_index] - milk[to_index]
    milk[to_index] = limits[to_index]
  return milk

def search(bucket_index, milk):
  indices = [0, 1, 2]
  indices.remove(bucket_index)
  if [bucket_index, milk] in calculated: return
  calculated.append([bucket_index, milk])
  for current_index in indices:
    current_milk = pour_milk(bucket_index, current_index, 
                              copy.copy(milk))
    if current_milk[0] == 0:
      milk_amounts.add(current_milk[2])
      #current_milk = pour_milk(indices[1 - current_index], 0, 
                              #current_milk)
      #if current_milk in calculated:
        #continue
    search(current_index, current_milk)
    search(indices[1 - indices.index(current_index)], current_milk)
    search(bucket_index, current_milk)

search(2, [0, 0, c])
sorted_milk = [str(i) for i in sorted(list(milk_amounts))]
fout.write(f"{' '.join(sorted_milk)}\n")
fin.close()
fout.close()
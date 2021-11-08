"""
ID: jujumoh1
LANG: PYTHON3
TASK: holstein
"""

import time, cProfile
t = time.time()

fin = open("holstein.in", "r")
fout = open("holstein.out", "w")

content = fin.read().splitlines()
v = int(content[0].strip())
vitamins = tuple([int(i) for i in content[1].strip().split()])
g = int(content[2].strip())
feeds = []
for line in content[3:]:
  feeds.append([int(i) for i in line.strip().split()])
count = [0]

memo = {}

def compare(sol1, sol2):
  if len(sol1) == 0:
    return sol2
  elif len(sol2) == 0:
    return sol1
  elif sol1[0] == -1:
    #if sol2[0] == -1:
      #return (-1,)
    return sol2
  elif sol2[0] == -1:
    return sol1
  elif len(sol1) > len(sol2):
    return sol2
  elif len(sol2) > len(sol1):
    return sol1

  sol1_vitamins = [0] * v
  sol2_vitamins = [0] * v
  for i in range(len(sol1)):
    for j in range(v):
      sol1_vitamins[j] += feeds[sol1[i] - 1][j]
      sol2_vitamins[j] += feeds[sol2[i] - 1][j]
  is_enough1 = True
  is_enough2 = True
  for i in range(v):
    if vitamins[i] > sol1_vitamins[i]:
      is_enough1 = False
    if vitamins[i] > sol2_vitamins[i]:
      is_enough2 = False
    if is_enough1 == False and is_enough2 == False: break
  else:
    if is_enough1 == True and is_enough2 == False:
      return sol1
    elif is_enough1 == False and is_enough2 == True:
      return sol2

  if sum(sol1) < sum(sol2):
    return sol1
  elif sum(sol1) == sum(sol2) and min(sol1) < min(sol2):
    return sol1
  return sol2
  #return (-1,)

def solve(feed_indexes):
  count[0] += 1
  if feed_indexes in memo:
    if memo[feed_indexes]:
      return feed_indexes
    return tuple()
  total = [0] * len(vitamins)
  for index in feed_indexes:
    for vitamin_ind, feed in enumerate(feeds[index - 1]):
      total[vitamin_ind] += feed
  for i in range(len(total)):
    if total[i] < vitamins[i]: break
  else:
    memo[feed_indexes] = True
    return feed_indexes
  memo[feed_indexes] = False

  best = tuple()
  for i in range(1, g + 1):
    if i in feed_indexes: 
      continue
    #elif len(feed_indexes) != 0:
      #if i == max(feed_indexes) + 1:
        #continue
    elif tuple(sorted(feed_indexes + (i,))) in memo:
      continue
    result = solve(tuple(sorted(feed_indexes + (i,))))
    best = compare(best, result)

  return best

solution = [str(i) for i in solve(tuple())]
fout.write(f"{len(solution)} {' '.join(solution)}\n")

fin.close()
fout.close()
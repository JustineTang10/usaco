"""
ID: jujumoh1
LANG: PYTHON3
TASK: zerosum
"""

fin = open("zerosum.in", "r")
fout = open("zerosum.out", "w")

n = int(fin.read().strip())
# calculated = set()
zero_sequences = []

def search(current_sum, count, operators, previous_number):
  """if (current_sum, count) in calculated:
    return"""
  if count == 0:
    if current_sum == 0:
      zero_sequences.append(operators)
    return

  # calculated.add((current_sum, count))
  search(current_sum - previous_number + int(str(previous_number) + str(len(operators) + 2)), count - 1, operators + [" "], int(str(previous_number) + str(len(operators) + 2)))
  search(current_sum + len(operators) + 2, count - 1, operators + ["+"], len(operators) + 2)
  search(current_sum - (len(operators) + 2), count - 1, operators + ["-"], -1 * (len(operators) + 2))

search(1, n - 1, [], 1)

for sequence in zero_sequences:
  for i in range(1, n):
    fout.write(f"{i}{sequence[i - 1]}")
  fout.write(f"{n}\n")

fin.close()
fout.close()
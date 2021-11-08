"""
ID: jujumoh1
LANG: PYTHON3
TASK: frac1
"""

fin = open('frac1.in', 'r')
fout = open('frac1.out', 'w')

n = int(fin.read().strip())

fout.write('0/1\n')

fractions_dict = {}
for i in range(2, n + 1):
  for j in range(i - 1, 0, -1):
    fractions_dict[(j, i)] = j / i

seen_values = set()
fractions = []
for key in fractions_dict:
  if not fractions_dict[key] in seen_values:
    fractions.append(key)
    seen_values.add(fractions_dict[key])

fractions.sort(key=lambda x: x[0] / x[1])

for fraction in fractions:
  fout.write(f'{fraction[0]}/{fraction[1]}\n')

fout.write('1/1\n')

fin.close()
fout.close()

""" // C
/*
ID: jujumoh1
LANG: C
TASK: frac1
*/

#include <stdio.h>
#include <stdlib.h>

int main(void) {
  FILE *fin = fopen("frac1.in", "r");
  FILE *fout = fopen("frac1.out", "w");
  int n, i, j;
  static int fractions[7807][2];
  int fraction_count = 0;
  int swap[2];
  fscanf(fin, "%d", &n);
  fprintf(fout, "0/1\n");
  for (i = 2; i <= n; i++)
    for (j = i; j > 0; j--) {
      if (i % j == 0 && j != 1)
        continue;
      fractions[fraction_count][0] = j;
      fractions[fraction_count][1] = i;
      fraction_count++;
    }
  for (i = 0; i < fraction_count; i++)
    for (j = i - 1; j >= 0; j--)
      if ((fractions[i][0] / fractions[i][1]) <
          (fractions[j][0] / fractions[j][1])) {
        swap[0] = fractions[i][0];
        swap[1] = fractions[i][1];
        fractions[i][0] = fractions[j][0];
        fractions[i][1] = fractions[j][1];
        fractions[j][0] = swap[0];
        fractions[j][1] = swap[1];
      }
  for (i = 0; i < fraction_count; i++)
    fprintf(fout, "%d/%d\n", fractions[i][0], fractions[i][1]);
  return 0;
}
"""
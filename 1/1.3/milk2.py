"""
ID: jujumoh1
LANG: PYTHON3
TASK: milk2
"""

fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

n = int(fin.readline().strip())
intervals = []
for _ in range(n):
  data = [int(j) for j in fin.readline().strip().split()]
  intervals.append(data)

intervals.sort(key=lambda x: x[0])

max_milk = 0
max_no_milk = 0
current_milk = 0
current_end = 0
if len(intervals) == 1:
  max_milk = intervals[0][1] - intervals[0][0]
else:
  for interval in intervals:
    if intervals.index(interval) == 0:
      current_milk += interval[1] - interval[0]
      current_end = interval[1]
    elif interval[0] > current_end:
      max_milk = max(max_milk, current_milk)
      max_no_milk = max(max_no_milk, interval[0] - current_end)
      current_end = interval[1]
      current_milk = interval[1] - interval[0]
    elif interval[1] > current_end:
      current_milk += interval[1] - current_end
      current_end = interval[1]

max_milk = max(max_milk, current_milk)
fout.write(f'{max_milk} {max_no_milk}\n')
fin.close()
fout.close()

""" // C version
/*
ID: jujumoh1
LANG: C
TASK: milk2
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct interval {
  int start;
  int end;
} interval;

int comparator(const void *p, const void *q) {
  int start1 = ((interval *)p)->start;
  int start2 = ((interval *)q)->start; 
  return (start1 - start2);
}

int main(void) {
  FILE *fin = fopen("milk2.in", "r");
  FILE *fout = fopen("milk2.out", "w");
  int n, i, max_milk, max_no_milk, cur_milk;
  int end = 0;
  fscanf(fin, "%d", &n);
  interval *intervals[n];
  for (i = 0; i < n; i++) {
    intervals[i] = malloc(sizeof(interval));
    if (intervals[i] == NULL) {
      fprintf(stderr, "malloc error");
      exit(1);
    }
    fscanf(fin, "%d%d", &intervals[i]->start, &intervals[i]->end);
    if (end < intervals[i]->end)
      end = intervals[i]->end;
  }
  qsort(intervals, n, sizeof(interval), comparator);
  max_milk = 0;
  max_no_milk = 0;
  cur_milk = intervals[0]->end - intervals[0]->start;
  if (n == 1)
    max_milk = cur_milk;
  else {
    for (i = 1; i < n; i++) {
      if (intervals[i]->start < intervals[i-1]->end &&
      intervals[i]->end > intervals[i-1]->end)
        cur_milk += intervals[i]->end - intervals[i-1]->end;
      else if (intervals[i]->start > intervals[i-1]->end) {
        if (cur_milk > max_milk)
          max_milk = cur_milk;
        if (intervals[i]->start - intervals[i-1]->end > 
            max_no_milk)
          max_no_milk = intervals[i]->start - intervals[i-1]->end;
      }
      if (intervals[i]->end == end) {
        if (cur_milk > max_milk)
          max_milk = cur_milk;
        break;
      }
    }
  }
  fprintf(fout, "%d %d\n", max_milk, max_no_milk);
  return 0;
} 
"""
"""
ID: jujumoh1
LANG: PYTHON3
TASK: wormhole
"""

def generate_pairs(given_points):
  all_points = []
  if len(given_points) == 2: return [[given_points]]
  for i in range(1, len(given_points)):
    new_points = []
    for j in range(1, len(given_points)):
      if i != j:
        new_points.append(given_points[j])
    current_points = generate_pairs(new_points)
    for p in current_points:
      p.append([given_points[0], given_points[i]])
      all_points.append(p)
  return all_points

def check_pairs(pairs, point):
  m = 1000000001
  found_pair = tuple()
  for pair in pairs:
    for pair_point in pair:
      if pair_point[0] > point[0] and pair_point[0] < m and pair_point[1] == point[1]:
        m = pair_point[0]
        found_pair = (pair, 1 - pair.index(pair_point))
  return found_pair

fin = open('wormhole.in', 'r')
fout = open('wormhole.out', 'w')

n = int(fin.readline().strip())
points = []
for _ in range(n):
  points.append([int(i) for i in fin.readline().strip().split()])
    
all_pairs = generate_pairs(points)
total = 0

for pairs in all_pairs:
  for pair in pairs:
    smaller_point = min(pair)
    found_pair = check_pairs(pairs, smaller_point)
    if not found_pair: continue
    if pair[0][1] == pair[1][1]:
      if found_pair[0][found_pair[1]] in pair:
        total += 1
        break
    while found_pair[0][found_pair[1]] != smaller_point:
      found_pair = check_pairs(pairs, found_pair[0][found_pair[1]])
      if not found_pair:
        break
    else:
      total += 1
      break

fout.write(f'{total}\n')
fin.close()
fout.close()

""" // C version
/*
ID: jujumoh1
LANG: C
TASK: wormhole
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*typedef struct point {
  int x;
  int y;
} point;*/

int check_pairs(int points[][2], int n, int start[], int end[]) {
  int total = 0, i, j, count;
  int start_point[2], end_point[2];
  start_point[0] = points[0][0];
  start_point[1] = points[0][1];
  printf("e\n");
  if (n > 2) {
    int new_points[n - 2][2];
    for (i = 0; i < n; i++) {
      count = 0;
      for (j = 1; j < n; j++) {
        if (i != j) {
          new_points[count][0] = points[j][0];
          new_points[count][1] = points[j][1];
          count++;
        }
        else {
          end_point[0] = points[j][0];
          end_point[1] = points[j][1];          
        }
      }
      total += check_pairs(new_points, n - 2, start_point, 
                            end_point);
    }
  }
  int current[2];
  return total;
}

int main(void) {
  FILE *fin = fopen("wormhole.in", "r");
  FILE *fout = fopen("wormhole.out", "w");
  int n, i;
  fscanf(fin, "%d", &n);
  int points[n][2], start[2], end[2];
  for (i = 0; i < n; i++) {
    fscanf(fin, "%d%d", &points[i][0], &points[i][1]);
    if (i == 0) {
      start[0] = points[i][0];
      start[1] = points[i][1];
    }
    else if (i == 1) {
      end[0] = points[i][0];
      end[1] = points[i][1];
    }
  }
  int total = check_pairs(points, n, start, end);
  fprintf(fout, "%d\n", total);
  return 0;
}
"""
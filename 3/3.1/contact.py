"""
ID: jujumoh1
LANG: PYTHON3
TASK: contact
"""

fin = open("contact.in", "r")
fout = open("contact.out", "w")

text = fin.read().splitlines()
a, b, n = [int(i) for i in text[0].split()]
sequence = "".join(text[1:])
frequencies = {}

for i in range(len(sequence)):
  for j in range(a, b + 1):
    if i + j <= len(sequence):
      frequencies.setdefault(sequence[i:i + j], 0)
      frequencies[sequence[i:i + j]] += 1

solutions = {}
for k, v in frequencies.items():
  solutions[v] = solutions.get(v, []) + [k]

count = 0
while len(solutions) > 0 and count < n:
  index = max(solutions.keys())
  fout.write(f"{index}")
  cur_frequency = solutions.pop(index)
  cur_frequency.sort()
  cur_frequency.sort(key=lambda x: len(x))
  for i in range(len(cur_frequency)):
    if i % 6 == 0:
      fout.write("\n")
    fout.write(f"{cur_frequency[i]}")
    if (i + 1) % 6 != 0 and i < len(cur_frequency) - 1:
      fout.write(" ")
  fout.write("\n")
  count += 1

fin.close()
fout.close()

""" // C
/*
ID: jujumoh1
LANG: C
TASK: contact
*/

#include <stdio.h>
#include <stdlib.h>

#define hashsize(n) ((unsigned long)1 << (n))
#define hashmask(n) (hashsize(n) - 1)
#define MAX_LENGTH 200000

typedef struct item {
  struct item* previous;
  char* string;
  int cur_num;
  int num_chars;
  struct item* next;
} item;

item* new_item(int num_chars) {
  item* i = malloc(sizeof(item));
  if (i == NULL) {
    fprintf(stderr, "malloc error\n");
    exit(1);
  }
  i->num_chars = num_chars;
  i->cur_num = 0;
  i->previous = NULL;
  i->next = NULL;
  i->string = malloc(sizeof(char) * 12);
  if (i->string == NULL) {
    fprintf(stderr, "malloc error\n");
    exit(1);
  }
  return i;
}

unsigned long oaat(char *key, unsigned long len) {
  unsigned long i;
  unsigned long hash = 0;
  for (i = 0; i < len; i++) {
    hash += key[i];
    hash += (hash << 10);
    hash ^= (hash >> 6);
  }
  hash += (hash << 3);
  hash ^= (hash >> 11);
  hash += (hash << 15);
  return hash & hashmask(13);
}

int main(void) {
  FILE *fin = fopen("contact.in", "r");
  FILE *fout = fopen("contact.out", "w");
  static item* table[8192];
  static char sequence[MAX_LENGTH];
  int a, b, n;
  fscanf(fin, "%d%d%d\n", &a, &b, &n);
  char current_char;
  int sequence_len = 0;
  while (fscanf(fin, "%c", &current_char) != EOF)
    if (current_char != '\n')
      sequence[sequence_len++] = current_char;
  int i, j;
  item *first_queue, *cur_queue, *prev_queue = NULL;
  for (i = 0; i < sequence_len; i++) {
    for (j = a; j <= b; j++)
      if (i + j <= sequence_len) {
        cur_queue = new_item(j);
        if (prev_queue == NULL)
          first_queue = cur_queue;
        else {
          prev_queue->next = cur_queue;
          cur_queue->previous = prev_queue;
        }
        prev_queue = cur_queue;
      }
    cur_queue = first_queue;
    while (cur_queue != NULL) {
      cur_queue->string[cur_queue->cur_num] = sequence[i];
      cur_queue->cur_num++;
      printf("%d\n", cur_queue->cur_num);
      if (cur_queue->cur_num == cur_queue->num_chars) {
        if (cur_queue == first_queue) {
          first_queue = first_queue->next;
          first_queue->previous = NULL;
        }
        else if (cur_queue->next == NULL)
          cur_queue->previous->next = NULL;
        else {
          cur_queue->previous->next = cur_queue->next;
          cur_queue->next->previous = cur_queue->previous;
        }
      }
      cur_queue = cur_queue->next;
    }
  }
  return 0;
}
"""
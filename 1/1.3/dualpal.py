"""
ID: jujumoh1
LANG: PYTHON3
TASK: dualpal
"""

fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')

n, s = [int(a) for a in fin.read().strip().split()]
digits = list('0123456789')
count = 0
current_number = s

while count < n:
  current_number += 1
  palindrome_count = 0
  for base in range(2, 11):
    number = current_number
    number_string = ''
    while number > 0:
      number_string += digits[int(number % base)]
      number = (number - (number % base)) / base
    if list(number_string) == list(reversed(number_string)):
      palindrome_count += 1
    if palindrome_count == 2:
      fout.write(f'{current_number}\n')
      count += 1
      break

fin.close()
fout.close()

""" // C version
/*
ID: jujumoh1
LANG: C
TASK: dualpal
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_palindrome(char number[]) {
  int start = 0, end = strlen(number) - 1;
  while (end - start >= 1) {
    if (number[start] != number[end])
      return 0;
    start++;
    end--;
  }
  return 1;
}

int main(void) {
  FILE *fin = fopen("dualpal.in", "r");
  FILE *fout = fopen("dualpal.out", "w");
  int base, convert_number, current_number, n, s;
  int count = 0, pal_count, convert_count;
  char digits[] = {'0', '1', '2', '3', '4', 
                    '5', '6', '7', '8', '9'};
  char number[10];
  fscanf(fin, "%d%d", &n, &s);
  current_number = s;
  while (count < n) {
    pal_count = 0;
    current_number += 1;
    for (base = 2; base <= 10; base++) {
      convert_number = current_number;
      convert_count = 0;
      while (convert_number > 0) {
        number[convert_count] = digits[convert_number % base];
        convert_number = (convert_number - 
                          (convert_number % base)) / base;
        convert_count++;
      }
      if (is_palindrome(number) == 1)
        pal_count++;
      memset(number, 0, strlen(number));
      if (pal_count >= 2) {
        count++;
        fprintf(fout, "%d\n", current_number);
        break;
      }
    }
  }
  return 0;
}
"""
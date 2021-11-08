"""
ID: jujumoh1
LANG: PYTHON3
TASK: palsquare
"""

fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')

base = int(fin.read().strip())
digits = list('0123456789ABCDEFGHIJ')

for i in range(1, 301):
  number = i
  number_string = ''
  while number > 0:
    number_string += digits[int(number % base)]
    number = (number - (number % base)) / base
  square = i * i
  square_string = ''
  while square > 0:
    square_string += digits[int(square % base)]
    square = (square - (square % base)) / base
  if list(square_string) == list(reversed(square_string)):
    number_string = ''.join(list(reversed(number_string)))
    fout.write(f'{number_string} {square_string}\n')

fin.close()
fout.close()

""" // C version
/*
ID: jujumoh1
LANG: C
TASK: palsquare
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_palindrome(char number[]) {
  int start = 0, end = strlen(number) - 1;
  while (end - start > 1) {
    if (number[start] != number[end])
      return 0;
    start++;
    end--;
  }
  return 1;
}

int main(void) {
  FILE *fin = fopen("palsquare.in", "r");
  FILE *fout = fopen("palsquare.out", "w");
  int base, count = 0, converting_number, i, j;
  char number[10], square[19], print_number[10], print_square[19];
  char digits[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', 
                    '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                    'I', 'J'};
  fscanf(fin, "%d", &base);
  for (i = 1; i <= 300; i++) {
    converting_number = i;
    while (converting_number > 0 && count < 9) {
      count++;
      number[9 - count] = digits[converting_number % base];
      converting_number = (converting_number - (converting_number % base)) / base;
    }
    count = 0;
    for (j = 0; j < 9; j++)
      if (number[j] != '\0') {
        print_number[count] = number[j];
        number[j] = NULL;
        count++;
      }
    printf("%s\n", number);
    converting_number = i * i;
    count = 0;
    while (converting_number > 0 && count < 18) {
      count++;
      square[18 - count] = digits[converting_number % base];
      converting_number = (converting_number - (converting_number % base)) / base;
    }
    count = 0;
    for (j = 0; j < 18; j++)
      if (square[j] != '\0') {
        print_square[count] = square[j];
        count++;
      }
    if (is_palindrome(print_square) == 1)
      fprintf(fout, "%s %s\n", print_number, print_square);
  }
  return 0;
}
"""
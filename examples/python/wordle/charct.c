// C program to implement
// the above approach
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int freq[26];
int dipth[26][26];

void init() {
  for (int i = 0; i < 26; i++) {
    freq[i] = 0;
    for (int j = 0; j < 26; j++) {
      dipth[i][j] = 0;
    }
  }
}

void ct_chars(char *word) {
  for (char* p = word; *p != '\0'; p++) {
    char c = *p;
    if (c >= 'a' && c <= 'z') {
      //printf("ct_word: char %c = %d\n", *p, *p);
      freq[c - 'a']++;
    }
  }
}

void ct_dipth(char *word) {
  int first = 1;
  char last = 0;
  for (char* p = word; *p != '\0'; p++) {
    char c = *p;
    if (c >= 'a' && c <= 'z') {
      if (first) {
        first = 0;
      } else {
        //printf("ct_word: char %c = %d\n", *p, *p);
        dipth[last - 'a'][c - 'a']++;
      }
      last = c;
    }
  }
}

void ct_word(char *word) {
  ct_chars(word);
  ct_dipth(word);
}

void print_freq() {
  printf("char frequency\n\n");
  for (char c = 'a'; c <= 'z'; c++) {
    printf("%4d %c\n", freq[c - 'a'], c);
  }
  printf("\ndipthong frequency\n\n");
  for (char c1 = 'a'; c1 <= 'z'; c1++) {
  for (char c2 = 'a'; c2 <= 'z'; c2++) {
    printf("%4d %c %c\n", dipth[c1 - 'a'][c2 - 'a'], c1, c2);
  }
  }
}

// Driver code
int main(int argc, char **argv)
{
  FILE* ptr;
  char str[500];

  if (argc < 2) {
    printf("usage: %s file\n", argv[0]);
    exit(0);
  }
  ptr = fopen(argv[1], "r");

  if (NULL == ptr) {
    printf("file '%s' can't be opened \n", argv[1]);
    exit(0);
  }

  init();

  printf("content of this file are \n");

  while (fgets(str, 500, ptr) != NULL) {
    //printf("%s", str);
    ct_word(str);
  }

  print_freq();
  fclose(ptr);
  return 0;
}

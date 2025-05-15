//fastgrep/c_lib/fastgrep.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 1024

//find substring(pattern) in a string(line)
int contains(const char *line, const char *pattern){
  return strstr(line, pattern) != NULL;
}

//searches a file and prints all instances of buffer which contain pattern in fineName
int searchFile(const char *fileName, const char *pattern){
  FILE *fp = fopen(fileName, "r");
  if (fp == NULL) return -1;
  char buffer[MAX_LINE];
  while(fgets(buffer, MAX_LINE, fp)){
    if(contains(buffer, patter))
      print("%s", buffer);
  }
  fclose(fp);
  return 0;
}


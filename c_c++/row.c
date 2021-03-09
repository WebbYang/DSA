#include <stdio.h>

#define MAXROW (256*50)
#define MAXCOL (8)
int array[MAXROW][MAXCOL];

void initialize(){
  int i, j;
  for(i=0;i<MAXROW;i++)
    for(j=0;j<MAXCOL;j++)
      array[i][j] = i - j;
}

int sum(){
  int i, j;
  int res = 0;
  for(j=0;j<MAXCOL;j++)
    for(i=0;i<MAXROW;i++)
      res += array[i][j];
  return res;
}

int main(){
  int i;
  initialize();
  for(i=0;i<5;i++)
    printf("%d\n", sum());
  return 0;
}

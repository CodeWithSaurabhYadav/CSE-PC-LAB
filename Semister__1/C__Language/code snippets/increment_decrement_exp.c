#include<stdio.h>

void main()
{
	int i = 0, j = 1;
	i = j++;
	printf("%d %d\n",i,j);
	i = 5 , j = 5;
	i = ++j;
	printf("%d %d\n",i,j);	
}

#include<stdio.h>

int main()
{
	/*code*/
	int a = 5 ,b = 6 ,c = 6;
	if (a<b && b!=a)
	{
		printf("Both Conditions are true [AND(&&)]\n");	
	}
	if (b<a || b==c)\
	{
		printf("Only one condition is true [OR(||)]\n");	
	}
	return 0;
}

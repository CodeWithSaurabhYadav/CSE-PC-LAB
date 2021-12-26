#include<stdio.h>

void main()
{
	//Enrolment Number
	printf("-----------------\n");
	printf("|202103103510362|\n");
	printf("-----------------\n");

	//Program
	int num1,num2,sum;
	printf("Enter number1: ");
	scanf("%d",&num1);
	printf("Enter number2: ");
	scanf("%d",&num2);
	sum = num1 + num2;
	printf("The addition of %d and %d is: %d\n",num1,num2,sum);
}

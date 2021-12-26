#include<stdio.h>

void main()
{
	//Enrolment Number
	printf("-----------------\n");
	printf("|202103103510362|\n");
	printf("-----------------\n");

	//VARIABLES
	float first,second;
	
	//Program
	printf("..................................................................\n");
	printf("\t\t\tCalculator\n");
	printf("..................................................................\n");
	printf("..................................................................\n");
	printf("Enter first number : ");
	scanf("%f",&first);
	printf("Enter first number : ");
	scanf("%f",&second);
	
	printf("\n..................................................................");
	printf("\nThe values of calculations are : \n");
	printf("..................................................................\n");
	
	//Division
	printf("The division of %f and %f is : %f\n\n",first,second,first/second);

	//Multiplication
	printf("The product of %f and %f is : %f\n\n",first,second,first*second);

	//Addition
	printf("The sum of %f and %f is : %f\n\n",first,second,first+second);
	

	//Substraction
	printf("The difference of %f and %f is : %f\n\n",first,second,first-second);
	
	printf("..................................................................\n");
}

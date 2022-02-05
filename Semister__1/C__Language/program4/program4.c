#include<stdio.h>

void main()
{
	//Enrolment Number
	printf("-----------------\n");
	printf("|202103103510362|\n");
	printf("-----------------\n");

	//Program
	float cel,fra;
	printf("Enter temperature into Frhrenheit : ");
	scanf("%f",&fra);
	fra = (fra-32)/1.8;
	printf("Temperature into Celsius is : %f \n",fra);
}

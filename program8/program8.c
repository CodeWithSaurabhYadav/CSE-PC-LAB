#include<stdio.h>
#include"enroll.h"
void main()
{
	//enrollment number
	enroll_print();

	//variables
	char day[10];
	int date,month,year;

	//code
	printf("Input the day, followed by date (dd-mm-yyyy) :\n");
	scanf("%s %d-%d-%d",day,&date,&month,&year);
	
	//Printing the values
	printf("\nDay : %s\n",day);
	printf("Date : %d\n",date);
	printf("Month : %d\n",month);
	printf("Year : %d\n",year);
}

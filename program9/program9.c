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
	scanf("%s %d-%d-%d",&day,&date,&month,&year);

    //if condition
    if (month == 1)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : January\n");
        printf("Year : %d\n",year);
    }
    else if (month == 2)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : Febuary\n");
        printf("Year : %d\n",year);
    }
    else if (month == 3)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : March\n");
        printf("Year : %d\n",year);
    }
    else if (month == 4)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : April\n");
        printf("Year : %d\n",year);
    }
    else if (month == 5)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : May\n");
        printf("Year : %d\n",year);
    }
    else if (month == 6)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : June\n");
        printf("Year : %d\n",year);
    }
    else if (month == 7)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : July\n");
        printf("Year : %d\n",year);
    }
    else if (month == 8)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : August\n");
        printf("Year : %d\n",year);
    }
    else if (month == 9)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : September\n");
        printf("Year : %d\n",year);
    }
    else if (month == 10)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : October\n");
        printf("Year : %d\n",year);
    }
    else if (month == 11)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : November\n");
        printf("Year : %d\n",year);
    }
    else if (month == 12)
    {
        //Printing the values
        printf("\nDay : %s\n",day);
        printf("Date : %d\n",date);
        printf("Month : December\n");
        printf("Year : %d\n",year);
    }
    else
    {
        printf("\nYou have entered invalid month number\n");
    }
        
}
    
	
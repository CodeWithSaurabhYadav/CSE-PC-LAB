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
        printf("\nDay : %s\nDate : %d\nMonth : January\nYear : %d\n",day,date,year);
    }
    else if (month == 2)
    {
        //Printing the values
        printf("\nDay : %s\nDate : %d\nMonth : Febuary\nYear : %d\n",day,date,year);
    }
    else if (month == 3)
    {
        //Printing the values
        printf("\nDay : %s\nDate : %d\nMonth : March\nYear : %d\n",day,date,year);
    }
    else if (month == 4)
    {
        //Printing the values
        printf("\nDay : %s\nDate : %d\nMonth : April\nYear : %d\n",day,date,year);
    }
    else if (month == 5)
    {
        //Printing the values
        printf("\nDay : %s\nDate : %d\nMonth : May\nYear : %d\n",day,date,year);
    }
    else if (month == 6)
    {
        //Printing the values
        printf("\nDay : %s\nDate : %d\nMonth : June\nYear : %d\n",day,date,year);
    }
    else if (month == 7)
    {
        //Printing the values
        printf("\nDay : %s\nDate : %d\nMonth : July\nYear : %d\n",day,date,year);
    }
    else if (month == 8)
    {
        //Printing the values
        printf("\nDay : %s\nDate : %d\nMonth : August\nYear : %d\n",day,date,year);
    }
    else if (month == 9)
    {
        //Printing the values
        printf("\nDay : %s\nDate : %d\nMonth : September\nYear : %d\n",day,date,year);
    }
    else if (month == 10)
    {
        //Printing the values
        printf("\nDay : %s\nDate : %d\nMonth : October\nYear : %d\n",day,date,year);
    }
    else if (month == 11)
    {
        //Printing the values
        printf("\nDay : %s\nDate : %d\nMonth : November\nYear : %d\n",day,date,year);
    }
    else if (month == 12)
    {
        //Printing the values
        printf("\nDay : %s\nDate : %d\nMonth : December\nYear : %d\n",day,date,year);
    }
    else
    {
        printf("\nYou have entered invalid month number\n");
    }
        
}
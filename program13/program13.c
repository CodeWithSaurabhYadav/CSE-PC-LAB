#include <stdio.h>
#include"enroll.h"

int main()
{
	enroll_print();
	int marks;
	printf("Enter your mark :");
	scanf("%d",&marks);
	if( marks >=26 && marks <=30)
	{
		printf("You got A grade in This Subject\n");
	}
	else if ( marks >=21 && marks <=25)
	{ 
		printf("You got B grade in This Subject\n");
	}
	else if ( marks >=14 && marks <=20)
	{
		printf("You got C grade in This Subject\n");
	}
        else if ( marks >=12 && marks <=13)
	{
		printf("You got D grade in This Subject\n");
	}
	else if ( marks <= 12)
	{
		printf("Sorry You are Failed in this Subject\n");
	}
    else printf("You have entered wrong marks.\n");
	return 0;
}




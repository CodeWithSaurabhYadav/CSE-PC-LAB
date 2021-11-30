#include <stdio.h>
#include "enroll.h"
void main()
{
    enroll_print();       
    int check, age;
    printf("Enter your age : ");
    check=scanf("%d",&age);
    if(check==0)
    {
        printf("You have not enterded valid age:\n");
    }
    if(check==1)
    {
        printf("You have lived for %d second\n",age*365*24*60*60);
    }
}
	

